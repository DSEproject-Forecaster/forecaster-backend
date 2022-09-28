from flask import Flask
from flask_cors import CORS
from Blueprints.dashboard import dashboard_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

if __name__ == '__main__':
   app.run(port=5050, debug=True)