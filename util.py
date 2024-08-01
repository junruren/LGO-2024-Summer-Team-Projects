# Utility Python code for Team MJJ's final projects
#
# To use what's inside here, simply:
#
# import util
#
# Like how we import other packages

import csv
import re

class Grid:
    def __init__(self, west_bound: float, east_bound: float, north_bound: float, south_bound: float) -> None:
        self.west_bound = west_bound
        self.east_bound = east_bound
        self.north_bound = north_bound
        self.south_bound = south_bound

    def __repr__(self) -> str:
        return (f"Grid(west_bound={self.west_bound}, east_bound={self.east_bound}, "
                f"north_bound={self.north_bound}, south_bound={self.south_bound})")

    def __eq__(self, other) -> bool:
        if not isinstance(other, Grid):
            return NotImplemented
        return (self.west_bound == other.west_bound and
                self.east_bound == other.east_bound and
                self.north_bound == other.north_bound and
                self.south_bound == other.south_bound)

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash((self.west_bound, self.east_bound, self.north_bound, self.south_bound))


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

def read_grid_definitions(csv_filename: str) -> list:
    """
    Read the CSV file, identified by the provided `csv_filename` and return a list of Grid objects.
    """
    with open(csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        results = [
            Grid(
                west_bound=float(row['West bound']),
                east_bound=float(row['East bound']),
                north_bound=float(row['North bound']),
                south_bound=float(row['South bound']),
            )
            for row in reader
        ]
    return results

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
