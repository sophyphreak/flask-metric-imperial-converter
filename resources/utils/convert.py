from measurement.measures import Weight, Volume, Distance


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
