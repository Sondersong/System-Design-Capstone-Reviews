import pandas as pd
import os
import psycopg2
from dotenv import load_dotenv

# load_dotenv()

# host = os.getenv('ADDRESS')
# host = os.getenv('USER')
# host = os.getenv('PASSWORD')

# connection = psycopg2.connect(host='localhost', dbname='SDC-Reviews', user='postgres', password='postgresPassword')

# cursor = connection.cursor()

test = pd.read_csv('ETL/data/SDC Application Data - Atelier Project (_Clean_ Data Set) 2/reviews.csv')

cleanDB = test.dropna(inplace=True)

print(cleanDB)