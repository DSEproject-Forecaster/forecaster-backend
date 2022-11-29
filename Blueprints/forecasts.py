from flask import Blueprint, jsonify
import db.dbHelper as db
from Utils.timeUtils import getCurrentTime
import datetime

forecasts_bp = Blueprint('forecasts', __name__)

@forecasts_bp.route('/getPredictions/', methods=['GET'])
def getDailySeasonalData():
    # curTime = getCurrentTime()
    curTime = "2021-01-10 03:00"
    base =  datetime.datetime.strptime(curTime, "%Y-%m-%d %H:%M")
    timestamps = [(base + datetime.timedelta(hours=x)).strftime("%Y-%m-%d %H:00:00") for x in range(24)]
    predictions = db.getPrediction(timestamps)
    return jsonify(predictions)