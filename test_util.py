import unittest
import util

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