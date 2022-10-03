import unittest
from src.ncatapi import NCAT
from src.Exceptions import RequiredParameterMissingException


class UtmRequestTests(unittest.TestCase):
    def test_it_should_raise_an_exception_if_required_parameters_are_missing_from_a_UTM_request(self):
        ncat = NCAT()
        try:
            ncat.utm({
                'northing': 4138641.144,
                'utmZone': 15,
                'spcZone': 2401,
                'inDatum': 'NAD83(2011)',
                'outDatum': 'NAD83(NSRS2007)'
            })
            self.fail('Failed to assert that the RequiredParameterMissingException was raised.')
        except RequiredParameterMissingException:
            self.assertRaises(RequiredParameterMissingException)
        except Exception as error:
            message = 'Wrong exception was raised: ' + type(error).__name__
            self.fail(message)

    def test_it_should_make_a_UTM_request_if_all_of_the_required_parameters_are_included(self):
        ncat = NCAT()
        response = ncat.utm({
            'northing': 4138641.144,
            'easting': 547883.655,
            'utmZone': 15,
            'spcZone': 2401,
            'inDatum': 'NAD83(2011)',
            'outDatum': 'NAD83(NSRS2007)'
        })
        self.assertEqual(response['srcDatum'], 'NAD83(2011)')


if __name__ == '__main__':
    unittest.main()
