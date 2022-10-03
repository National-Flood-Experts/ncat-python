import unittest
from src.ncatapi import NCAT


class NCATTests(unittest.TestCase):
    def test_it_should_take_any_parameters_and_convert_them_to_a_query_string(self):
        ncat = NCAT()
        query_string = ncat._NCAT__build_query_string({
            'lat': 39.2240867222,
            'lon': -98.5421515000,
            'orthoHt': 100,
            'inDatum': 'NAD83(1986)',
            'outDatum': 'NAD83(2011)',
            'inVertDatum': 'NGVD29',
            'outVertDatum': 'NAVD88'
        })
        self.assertEqual(query_string, 'lat=39.2240867222&lon=-98.5421515&orthoHt=100&inDatum=NAD83(1986)&outDatum=NAD83(2011)&inVertDatum=NGVD29&outVertDatum=NAVD88')


if __name__ == '__main__':
    unittest.main()
