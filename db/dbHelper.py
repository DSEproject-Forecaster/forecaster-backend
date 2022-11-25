from pymongo import MongoClient

def readDailySeasonality():
    collection = db['daily_seasonality']
    return collection.find_one({})

def readYearlySeasonality():
    collection = db['yearly_seasonality']
    return collection.find_one({})

def readTrends():
    collection = db['trends']
    return collection.find_one({})

def readWeatherData():
    collection = db['weather']
    return collection.find_one({})
    
client = MongoClient("mongodb+srv://dseproject:52WZZNOI1sqoiQ2u@cluster0.eeo6x3p.mongodb.net/?retryWrites=true&w=majority")
db = client.test