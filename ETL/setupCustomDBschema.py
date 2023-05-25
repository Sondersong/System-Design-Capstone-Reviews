import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('ADDRESS')
user = os.getenv('ACCOUNT')
password = os.getenv('PASSWORD')

connection = psycopg2.connect(host=host, dbname='SDC-Reviews', user=user, password=password)

cursor = connection.cursor()

f = open('ETL/RawDataStructure.sql', 'r')
schema = f.read()
f.close

schemaCommands = schema.split(';')

for command in schemaCommands:
  if command:
    try:
      cursor.execute(command)
    except:
      print('ERROR - The server is probs already defined')
      break

connection.commit()

connection.close()