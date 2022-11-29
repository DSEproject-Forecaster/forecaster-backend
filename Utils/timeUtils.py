from datetime import datetime
import pytz

def getCurrentTime():
    claytonTZ = pytz.timezone("Australia/Melbourne") 
    timeInNewYork = datetime.now(claytonTZ)
    currentTime = timeInNewYork.strftime("%Y-%m-%d %H:00")
    return currentTime