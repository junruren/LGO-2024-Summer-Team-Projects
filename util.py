# Utility Python code for Team MJJ's final projects
#
# To use what's inside here, simply:
#
# import util
#
# Like how we import other packages

import re

class Grid:
    def __init__(self, west_bound: float, east_bound: float, north_bound: float, south_bound: float) -> None:
        self.west_bound = west_bound
        self.east_bound = east_bound
        self.north_bound = north_bound
        self.south_bound = south_bound

    def contains(self, latitude: float, longitude: float) -> bool:
        """
        Check if this Grid cell contains the given point, represented by the `latitude` and `longitude`. Return True if
        yes, False otherwise.

        To have a consistent tie-breaking, east_bound and north_bound are compared inclusively while east_bound and
        south_bound are not. Mathmatically, this function evaluates:
        (south_bound < latitude <= north_bound) AND (west_bound < longitude <= east_bound)
        That is, if a given latitude precisely equals to the `south_bound`, the point is considered *not* contained in
        the Grid.
        """
        return (
            (self.south_bound < latitude and latitude <= self.north_bound)
            and
            (self.west_bound < longitude and longitude <= self.east_bound)
        )

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
