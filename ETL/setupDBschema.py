import csv
import psycopg2

connection = psycopg2.connect(host='localhost', dbname='SDC-Reviews', user='postgres', password='postgresPassword')

cursor = connection.cursor()

f = open('./Reviews-Schema.sql', 'r')
schema = f.read()
f.close

schemaCommands = schema.spl(';')

for command in schemaCommands:
  cursor.execute(command)

connection.commit()

connection.close()