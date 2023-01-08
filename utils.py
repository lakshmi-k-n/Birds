from iso3166 import countries
import re

def is_valid_country_code(country_code):
    try:
        countries.get(country_code)
    except KeyError:
        return False
    return True

def validate_longitude(longitude):
    if re.fullmatch("^(\+|-)?(?:180(?:(?:\.0{1,6})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,6})?))$", longitude):
        return True
    else:
        raise False

def validate_latitude(latitude):
    if re.fullmatch("^(\+|-)?(?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,6})?))$", latitude):
        return True
    else:
        raise False

def is_valid_coordinates(latitude, longitude):
    return validate_latitude(latitude) and \
                        validate_longitude(longitude)
