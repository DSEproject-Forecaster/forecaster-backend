from flask import Flask
from flask_cors import CORS
from Blueprints.dashboard import dashboard_bp
from Blueprints.forecasts import forecasts_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(forecasts_bp, url_prefix='/forecasts')

if __name__ == '__main__':
   app.run(port=5050, debug=True)