# Utility Python code for Team MJJ's final projects
#
# To use what's inside here, simply:
#
# import util
#
# Like how we import other packages

import re

def parse_coordinates(address: str):
    """
    Given location string value that contains coordinates (and other text), return the parsed latitude and longitude as
    a tuple.
    """
    # Regular expression to match the latitude and longitude
    coordinate_pattern = r'\((-?\d+\.\d+),\s*(-?\d+\.\d+)\)'
    
    # Search for the pattern in the address string
    match = re.search(coordinate_pattern, address)
    
    if match:
        # Extract latitude and longitude from the matched groups
        latitude = float(match.group(1))
        longitude = float(match.group(2))
        return (latitude, longitude)
    else:
        raise ValueError("No coordinates found in the given string")