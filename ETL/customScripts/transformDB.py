import pandas as pd

file = pd.read_csv('ETL/data/rawData/reviews_photos.csv')

file.rename(columns={"review_id": "ReviewID"})

file.to_csv('ETL/data/cleanData/photos.csv', index=False)