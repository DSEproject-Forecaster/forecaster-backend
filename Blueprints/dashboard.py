from flask import Blueprint, jsonify
import pandas as pd
from random import randint

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/getDailySeasonalData/', methods=['GET'])
def getDailySeasonalData():
    daily_df = pd.read_csv('./static/csv/daily_seasonal.csv')

    out = {
        'labels': daily_df.index.tolist(),
        'datasets': [],
        'borderColor': ''
    }

    for col in daily_df.columns:
        r = randint(0, 255)
        g = 255 - r
        b = randint(0, 255)
        out['datasets'].append({
            'label': col,
            'data': daily_df[col].values.tolist(),
            'borderColor':'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')'
        })
    return jsonify(out)

@dashboard_bp.route('/getYearlySeasonalData/', methods=['GET'])
def getYearlySeasonalData():
    yearly_df = pd.read_csv('./static/csv/yearly_seasonal.csv')

    out = {
        'labels': yearly_df.index.tolist(),
        'datasets': [],
        'borderColor': ''
    }

    for col in yearly_df.columns:
        r = randint(0, 255)
        g = 255 - r
        b = randint(0, 255)
        out['datasets'].append({
            'label': col,
            'data': yearly_df[col].values.tolist(),
            'borderColor':'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')'
        })
    return jsonify(out)

@dashboard_bp.route('/getTrends/', methods=['GET'])
def getTrends():
    trend_df = pd.read_csv('./static/csv/trends.csv')

    out = {
        'labels': trend_df.index.tolist(),
        'datasets': [],
        'borderColor': ''
    }

    for col in trend_df.columns:
        r = randint(0, 255)
        g = 255 - r
        b = randint(0, 255)
        out['datasets'].append({
            'label': col,
            'data': trend_df[col].values.tolist(),
            'borderColor':'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')'
        })
    return jsonify(out)