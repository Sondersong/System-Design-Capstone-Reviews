import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('ADDRESS')
user = os.getenv('ACCOUNT')
password = os.getenv('PASSWORD')

connection = psycopg2.connect(host=host, dbname='SDC-Reviews', user=user, password=password)

cursor = connection.cursor()

with open('ETL/data/usableData/characteristic_reviews.csv', 'r') as file:
    next(file)
    cursor.copy_from(file, 'testTable', sep=',')

connection.commit()
cursor.close()
connection.close()