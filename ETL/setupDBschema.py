import csv
import psycopg2

connection = psycopg2.connect(host='localhost', dbname='SDC-Reviews', user='postgres', password='postgresPassword')

cursor = connection.cursor()

f = open('ETL/Reviews-Schema.sql', 'r')
schema = f.read()
f.close

schemaCommands = schema.split(';')


for command in schemaCommands:
  if command:
    try:
      cursor.execute(command)
    except:
      print('The serve is probs already defined')

connection.commit()

connection.close()