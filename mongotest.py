from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb+srv://dseproject:52WZZNOI1sqoiQ2u@cluster0.eeo6x3p.mongodb.net/?retryWrites=true&w=majority")
db = client.test

daily_df = pd.read_csv('./static/csv/daily_seasonal.csv')
data = daily_df.to_dict(orient="list")
db.daily_seasonality.insert_many([data])

yearly_df = pd.read_csv('./static/csv/yearly_seasonal.csv')
data = yearly_df.to_dict(orient="list")
db.yearly_seasonality.insert_many([data])


trend_df = pd.read_csv('./static/csv/trends.csv')
data = trend_df.to_dict(orient="list")
db.trends.insert_many([data])

df = pd.read_csv('./static/csv/weather.csv')
data = df.to_dict(orient="list")
db.weather.insert_many([data])