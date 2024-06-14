import os
import pandas as pd
import psycopg2
import argparse
from dotenv import load_dotenv

load_dotenv()


def run_query_and_save_to_excel(query, conn, xlsx_path):
    """
    Executes a SQL query and saves the result to an Excel file.

    Parameters:
        query (str): SQL query to execute
        conn (psycopg2.connection): Active connection to the PostgreSQL database
        xlsx_path (str): Path where the Excel file will be saved

    Returns:
        None
    """
    df = pd.read_sql_query(query, conn)
    df.to_excel(xlsx_path, index=False)


def convert_sql_to_xlsx(sql_in, xlsx_out, xlsx_name=None):
    """
    This sets the output file to whatever the input filename was, just 
    replaces the .SQL with .XLSX

    Parameters:
        sql_in (str): relative filepath to .sql file
        xlsx_out (str): relative filepath to directory where .xlsx will be stored
        xlsx_name (str or None): If not None, file named xlsx_name.xlsx
                                 If None, file named same as sql_in

    Returns:
        None
    """
    with open(sql_in, 'r') as file:
        query = file.read()

    if xlsx_name is None:
        xlsx_name = os.path.basename(sql_in).replace('.sql', '.xlsx')

    xlsx_path = os.path.join(xlsx_out, xlsx_name)

    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

    run_query_and_save_to_excel(query, conn, xlsx_path)
    conn.close()


def convert_directory_of_queries(sql_in_dir, xlsx_out_dir):
    """
    Runs each query in sql_in_dir directory,
        stores each result as .xlsx in xlsx_out_dir.

    Parameters:
        sql_in_dir (str): relative filepath to directory
                          containing .sql files
        xlsx_out_dir (str): relative filepath to directory
                            where .xlsx will be stored
                            files named same as sql_in

    Returns:
        None
    """
    for sql_file in os.listdir(sql_in_dir):
        if sql_file.endswith(".sql"):
            sql_path = os.path.join(sql_in_dir, sql_file)
            convert_sql_to_xlsx(sql_path, xlsx_out_dir)


def convert_sql_to_xlsx_from_cli():
    """
    Runs a directory of SQL files and saves the output as Excel.
    """
    parser = argparse.ArgumentParser(
        description="Run SQL files and save the output to Excel.",
        epilog="Examples:\n"
               "  Convert a single SQL file:\n"
               "    python run_query.py -f path/to/sqlfile.sql -o path/to/output_directory\n"
               "  Convert all SQL files in a directory:\n"
               "    python run_query.py -d path/to/sql_directory -o path/to/output_directory",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-f', '--file', type=str,
                        help="Single .sql file to convert")
    parser.add_argument('-d', '--directory', type=str,
                        help="Directory containing .sql files")
    parser.add_argument('-o', '--output', type=str,
                        required=True, help="Directory to save .xlsx files")

    args = parser.parse_args()

    # Ensure the output directory exists, and if not then create it
    os.makedirs(args.output, exist_ok=True)

    if args.directory:
        convert_directory_of_queries(args.directory, args.output)
    elif args.file:
        convert_sql_to_xlsx(args.file, args.output)
    else:
        print("Either --directory or --file must be specified.")


if __name__ == "__main__":
    convert_sql_to_xlsx_from_cli()
