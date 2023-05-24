import pandas as pd
import sqlalchemy
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('ADDRESS')
user = os.getenv('ACCOUNT')
password = os.getenv('PASSWORD')

connection = sqlalchemy.create_engine('postgresql://{2}:{0}@{1}:5432/SDC-Reviews'.format(password, host, user))

fs = pd.read_csv('ETL/data/usableData/characteristic_reviews.csv')

print(fs)

# fs.to_sql('testTable', connection, if_exists='replace', chunksize='100')