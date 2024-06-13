import psycopg2 as pg2
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

##### SET UP ENVIRONMENT #####
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

##### CONNECT TO DB #####
conn = pg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

c = conn.cursor()


#### INSERT YOUR QUERY ######
query = '''

'''

#### RUN THE QUERY ######
result_df = pd.read_sql(query, conn)


#### OUTPUT REPORT ######
output_file_csv = 'excel_reports/Q1_HR_Report.csv'
result_df.to_csv(output_file_csv, index=False)

#### CLOSE THE CONNECTION ######
conn.close()
