import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('ADDRESS')
user = os.getenv('ACCOUNT')
password = os.getenv('PASSWORD')

connection = psycopg2.connect(host=host, dbname='Raw-SDC-Reviews', user=user, password=password)

cursor = connection.cursor()

with open('ETL/data/rawData/characteristic_reviews.csv', 'r') as file:
    next(file)
    cursor.copy_from(file, 'Characteristic_Reviews', sep=',')

with open('ETL/data/rawData/characteristics.csv', 'r') as file:
    next(file)
    cursor.copy_from(file, 'Characteristics', sep=',')

with open('ETL/data/rawData/reviews_photos.csv', 'r') as file:
    next(file)
    cursor.copy_from(file, 'Reviews_Photos', sep=',')

with open('ETL/data/rawData/reviews.csv', 'r') as file:
    next(file)
    cursor.copy_from(file, 'Reviews', sep=',')

connection.commit()
cursor.close()
connection.close()