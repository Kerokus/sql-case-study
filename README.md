# sql-case-study

The ```run_query.py``` contains functions designed to execute SQL queries and saves the outputs of those queries into ```.xlsx``` files 

## Libraries
 os 

 pandas

 psycopg2

 argparse
 
 dotenv
 
## Functions

### run_query_and_save_to_excel
```run_query_and_save_to_excel``` uses pandas to execute an SQL query 
and save the results to an Excel file.

### convert_sql_to_xlsx
```convert_sql_to_xlsx``` sets the ouput filename to be the same as the input filename other than the filetype

### convert_directory_of_queries
```convert_directory_of_queries``` runs each query in sql_in_dir directory,
stores each result as ```.xlsx``` in xlsx_out_dir.

### convert_sql_to_xlsx_from_cli
```convert_sql_to_xlsx_from_cli``` runs a directory of ```.sql``` files and saves the output as Excel

```-f``` or ```--file``` will allow this function to be ran on a single ```.sql``` file

```-d``` or ```--directory``` will allow this function to be ran on a directory of ```.sql``` files

```-o``` or ```--output``` will allow this function to direct its output to a directory of ```.xlsx``` files