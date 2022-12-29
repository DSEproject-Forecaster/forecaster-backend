from flask import Blueprint, jsonify
import db.dbHelper as db
from Utils.timeUtils import getCurrentTime
from dateutil.relativedelta import relativedelta
import datetime
import pandas as pd

forecasts_bp = Blueprint('forecasts', __name__)

@forecasts_bp.route('/getPredictions/', methods=['GET'])
def getPredictions():
    curTime = getCurrentTime()
    # curTime = "2021-01-10 03:00"
    base =  datetime.datetime.strptime(curTime, "%Y-%m-%d %H:%M")
    timestamps = [(base + datetime.timedelta(hours=x)).strftime("%Y-%m-%d %H:00:00") for x in range(24)]
    predictions = db.getPrediction(timestamps)
    return jsonify(predictions)

@forecasts_bp.route('/getWeeklyPredictions/', methods=['GET'])
def getWeeklyPredictions():
    curTime = getCurrentTime()
    base =  datetime.datetime.strptime(curTime, "%Y-%m-%d %H:%M")
    timestamps = [(base + datetime.timedelta(days=x)).strftime("%Y-%m-%d %H:00:00") for x in range(7)]
    predictions = db.getPrediction(timestamps)
    return jsonify(predictions)

@forecasts_bp.route('/getMonthlyRadar/', methods=['GET'])
def getMonthlyRadar():
    curTime = getCurrentTime()
    base =  datetime.datetime.strptime(curTime, "%Y-%m-%d %H:%M")
    timestamps = [(base + relativedelta(months=+x)).strftime("%Y-%m-%d %H:00:00") for x in range(12)]
    predictions = db.getPrediction(timestamps)
    out=[]
    attributes = list(predictions[0].keys())
    attributes.remove('time_stamp')

    theta = []
    for timestamp in timestamps:
        theta.append(datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").strftime('%b %y'))

    for col in attributes:
        vals=[]
        for month in predictions:
            vals.append(month[col])
        trace = {
            'type': 'scatterpolar',
            'r': vals + [vals[0]],
            'theta': theta + [theta[0]],
            'name': col
        }
        out.append(trace)
    return jsonify(out)