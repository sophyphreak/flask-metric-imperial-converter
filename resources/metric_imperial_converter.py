from flask_restful import Resource, reqparse
from measurement.measures import Weight, Volume, Distance
import re

from .utils.get_return_dict import get_return_dict

class MetricImperialConverter(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('input', 
        type=str,
        location='args',
        required=True,
        help="input is required"
    )
    def get(self):
        data = MetricImperialConverter.parser.parse_args()
        _input = data['input']

        first_letter_index = re.search('[a-zA-Z]', _input).start()
        initial_unit = _input[first_letter_index:]

        try:
            initial_number = get_initial_number(_input, first_letter_index)
        except:
            return get_error(initial_unit)
        if not is_valid_unit(initial_unit):
            return {"error": "invalid unit"}

        return get_return_dict(initial_unit, initial_number)

def get_initial_number(_input, first_letter_index):
    raw_number = _input[:first_letter_index]
    if not raw_number:
        number = 1
    else:
        number = eval(raw_number)
    return number

def get_error(initial_unit):
    if is_valid_unit(initial_unit):
        return {"error": "invalid number"}
    return {"error": "invalid number and unit"}

def is_valid_unit(initial_unit):
    return initial_unit in ['kg', 'lbs', 'L', 'gal', 'mi', 'km']
