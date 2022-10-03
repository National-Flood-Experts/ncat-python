import unittest
from src.Exceptions import RequiredParameterMissingException
from src.ncatapi import NCAT


class LLHTests(unittest.TestCase):
    def test_it_should_raise_an_exception_if_required_parameters_are_missing_from_a_LLH_request(self):
        ncat = NCAT()
        try:
            ncat.llh({
                'lat': 40.0,
                'eht': 100.0,
                'inDatum': 'NAD83(1986)',
                'outDatum': 'NAD83(2011)'
            })
            self.fail('Failed to assert that the RequiredParameterMissingException was raised.')
        except RequiredParameterMissingException:
            self.assertRaises(RequiredParameterMissingException)
        except Exception as error:
            message = 'Wrong exception was raised: ' + type(error).__name__
            self.fail(message)

    def test_it_should_make_a_LLH_request_if_all_of_the_required_parameters_are_included(self):
        ncat = NCAT()
        response = ncat.llh({
            'lat': 40.0,
            'lon': -80.0,
            'orthoHt': 99.0,
            'inDatum': 'nad83(1986)',
            'outDatum': 'nad83(2011)',
            'inVertDatum': 'NGVD29',
            'outVertDatum': 'NAVD88'
        })
        self.assertAlmostEqual(float(response['srcLat']), 40.0)
        self.assertAlmostEqual(float(response['srcLon']), -80.0)


if __name__ == '__main__':
    unittest.main()
