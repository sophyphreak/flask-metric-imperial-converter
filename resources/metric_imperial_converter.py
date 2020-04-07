from flask_restful import Resource, reqparse
from measurement.measures import Weight, Volume, Distance
import re

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

def get_return_dict(initial_unit, initial_number):
    if initial_unit == 'kg':
        return_unit = 'lbs'
        return_number = convert_kg_to_lbs(initial_number)
        initial_string = f'{initial_number} kilograms'
        return_string = f'{return_number} pounds'

    if initial_unit == 'lbs':
        return_unit = 'kg'
        return_number = convert_lbs_to_kg(initial_number)
        initial_string = f'{initial_number} pounds'
        return_string = f'{return_number} kilograms'

    if initial_unit == 'L':
        return_unit = 'gal'
        return_number = convert_L_to_gal(initial_number)
        initial_string = f'{initial_number} liters'
        return_string = f'{return_number} gallons'

    if initial_unit == 'gal':
        return_unit = 'L'
        return_number = convert_gal_to_L(initial_number)
        initial_string = f'{initial_number} gallons'
        return_string = f'{return_number} liters'

    if initial_unit == 'mi':
        return_unit = 'km'
        return_number = convert_mi_to_km(initial_number)
        initial_string = f'{initial_number} miles'
        return_string = f'{return_number} kilometers'

    if initial_unit == 'km':
        return_unit = 'mi'
        return_number = convert_km_to_mi(initial_number)
        initial_string = f'{initial_number} kilometers'
        return_string = f'{return_number} miles'

    return {"initNum": initial_number, "initUnit": initial_unit, "returnNum": return_number, "returnUnit": return_unit, "string": f'{initial_string} converts to {return_string}'}

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

def convert_kg_to_lbs(initial_number):
    return round(Weight(kg=initial_number).lb, 5)

def convert_lbs_to_kg(initial_number):
    return round(Weight(lb=initial_number).kg, 5)

def convert_mi_to_km(initial_number):
    return round(Distance(mi=initial_number).km, 5)

def convert_km_to_mi(initial_number):
    return round(Distance(km=initial_number).mi, 5)

def convert_L_to_gal(initial_number):
    return round(Volume(l=initial_number).us_g, 5)

def convert_gal_to_L(initial_number):
    return round(Volume(us_g=initial_number).l, 5)

