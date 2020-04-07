from .convert import convert_kg_to_lbs, convert_lbs_to_kg, convert_L_to_gal, convert_gal_to_L, convert_mi_to_km, convert_km_to_mi

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
