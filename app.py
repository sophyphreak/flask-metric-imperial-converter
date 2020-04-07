from flask import Flask
from flask_restful import Api
from flask_talisman import Talisman

from resources.metric_imperial_converter import MetricImperialConverter

app = Flask(__name__)
Talisman(app)
api = Api(app)

api.add_resource(MetricImperialConverter, '/api/convert/')

if __name__ == '__main__':
    app.run(debug=True)