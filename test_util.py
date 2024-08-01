import unittest
import util

class TestGridClass(unittest.TestCase):

    def test_equality(self):
        grid1 = util.Grid(
            west_bound=-71.113,
            east_bound=-71.089,
            north_bound=42.391,
            south_bound=42.378
        )
        grid2 = util.Grid(
            west_bound=-71.113,
            east_bound=-71.089,
            north_bound=42.391,
            south_bound=42.378
        )
        self.assertEqual(grid1, grid2)
        grid3 = util.Grid(
            west_bound=-71.11,
            east_bound=-71.089,
            north_bound=42.391,
            south_bound=42.378
        )
        self.assertNotEqual(grid1, grid3)

    def test_contains(self):
        latitude = 42.378741522
        longitude = -71.110071228
        # Cell Number 7
        test_grid = util.Grid(
            west_bound=-71.113,
            east_bound=-71.089,
            north_bound=42.391,
            south_bound=42.378
        )
        self.assertTrue(test_grid.contains(latitude, longitude))

        # north_bound and east_bound are compared *inclusively*
        latitude = 42.391
        longitude = -71.089
        self.assertTrue(test_grid.contains(latitude, longitude))
        # west_bound is not compared *inclusively*
        latitude = 42.378741522
        longitude = -71.113
        self.assertFalse(test_grid.contains(latitude, longitude))
        # south_bound is not compared *inclusively*
        latitude = 42.378
        longitude = -71.110071228
        self.assertFalse(test_grid.contains(latitude, longitude))


class TestParsingMethods(unittest.TestCase):

    def test_parse_coordinates(self):
        location = '''8 SCOTT ST
        Cambridge, MA
        (42.378741522, -71.110071228)'''
        self.assertEqual(util.parse_coordinates(location), (42.378741522, -71.110071228))

        # check that util.parse_coordinates fails when no coordinates are found
        with self.assertRaises(ValueError):
            location = '''8 SCOTT ST
            Cambridge, MA'''
            util.parse_coordinates(location)

        with self.assertRaises(ValueError):
            location = '''8 SCOTT ST
            Cambridge, MA
            (42.378741522 -71.110071228)'''
            util.parse_coordinates(location)

        with self.assertRaises(ValueError):
            location = '''8 SCOTT ST
            Cambridge, MA
            (-71.110071228)'''
            util.parse_coordinates(location)

        with self.assertRaises(ValueError):
            location = '''8 SCOTT ST
            Cambridge, MA
            42.378741522, -71.110071228'''
            util.parse_coordinates(location)

if __name__ == '__main__':
    unittest.main()