from flask import Blueprint, jsonify, request
import pandas as pd
from random import randint
from pymongo import MongoClient
import db.dbHelper as db

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/getDailySeasonalData/', methods=['GET'])
def getDailySeasonalData():
    daily_df = pd.DataFrame.from_dict(db.readDailySeasonality()).drop("_id", axis=1)

    out = []

    for col in daily_df.columns:
        trace = {
            'x': [i for i in range(24)],
            'y': daily_df[col].values.tolist(),
            'mode': 'lines',
            'name': col
        }
        out.append(trace)
    return jsonify(out)

@dashboard_bp.route('/getYearlySeasonalData/', methods=['GET'])
def getYearlySeasonalData():
    yearly_df = pd.DataFrame.from_dict(db.readYearlySeasonality()).drop("_id", axis=1)

    out = []

    colList = list(yearly_df.columns)
    colList.remove('time_stamp')

    for col in colList:
        trace = {
            'x': yearly_df.time_stamp.values.tolist(),
            'y': yearly_df[col].values.tolist(),
            'type': "scatter",
            'mode': "lines",
            'name': col
        }
        out.append(trace)
    return jsonify(out)

@dashboard_bp.route('/getTrends/', methods=['GET'])
def getTrends():
    trend_df = pd.DataFrame.from_dict(db.readTrends()).drop("_id", axis=1)

    out = []

    colList = list(trend_df.columns)
    colList.remove('time_stamp')

    for col in colList:
        trace = {
            'x': trend_df.time_stamp.values.tolist(),
            'y': trend_df[col].values.tolist(),
            'type': "scatter",
            'mode': "lines",
            'name': col
        }
        out.append(trace)
    return jsonify(out)

@dashboard_bp.route('/getCorrelations/', methods=['GET'])
def getCorrelations():
    df = pd.DataFrame.from_dict(db.readWeatherData()).drop("_id", axis=1)

    out = [
        {
            'z': df.corr().to_numpy().tolist(),
            'x': list(df.columns),
            'y': list(df.columns),
            'type': 'heatmap'
        }
    ]

    return jsonify(out)

@dashboard_bp.route('/getBoxPlots/', methods=['GET'])
def getBoxPlots():
    df = pd.DataFrame.from_dict(db.readWeatherData()).drop("_id", axis=1)

    out = []

    for col in df.columns:
        trace = {
            'y': df[col].values.tolist(),
            'type': 'box',
            'name': col
        }
        out.append(trace)

    return jsonify(out)

@dashboard_bp.route('/getRadar/', methods=['GET'])
def getRadar():
    year = request.args.get('year')
    df = pd.DataFrame.from_dict(db.readWeatherData()).drop("_id", axis=1)
    df['time_stamp'] = pd.to_datetime(df['time_stamp'])

    df = df[df['time_stamp'].dt.year==int(year)]
    # df2 = df.iloc[-1]
    # df.append(df2)
    # print(df2.shape, df.shape)
    out = []

    colList = list(df.columns)
    colList.remove('time_stamp')
    
    for col in colList:
        trace = {
            'type': 'scatterpolar',
            'r': df[col].values.tolist(),
            'theta': ['Jan','Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
            'name': col
        }
        out.append(trace)

    return jsonify(out)