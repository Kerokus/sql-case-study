import psycopg2 as pg2
import pandas as pd
from dotenv import load_dotenv
import os


DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Connect to the PostgreSQL database
conn = pg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

c = conn.cursor()

query = '''
INSERT SQL QUERY HERE
'''
