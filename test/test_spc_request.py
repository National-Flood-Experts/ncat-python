import unittest
from src.ncatapi import NCAT
from src.Exceptions import RequiredParameterMissingException


class SPCRequestTests(unittest.TestCase):
    def test_it_should_throw_an_error_if_required_parameters_are_missing_from_a_SPC_request(self):
        ncat = NCAT()
        try:
            ncat.spc({
                'northing': 173099.419,
                'easting': 503626.812,
                'inDatum': 'nad83(2011)',
                'outDatum': 'nad83(2007)'
            })
            self.fail('Failed to assert that the RequiredParameterMissingException was raised.')
        except RequiredParameterMissingException:
            self.assertRaises(RequiredParameterMissingException)
        except Exception as error:
            message = 'Wrong exception was raised: ' + type(error).__name__
            self.fail(message)

    def test_it_should_make_a_SPC_request_if_all_of_the_required_parameters_are_included(self):
        ncat = NCAT()
        response = ncat.spc({
            'northing': 173099.419,
            'easting': 503626.812,
            'spcZone': 2402,
            'inDatum': 'nad83(2011)',
            'outDatum': 'nad83(NSRS2007)'
        })
        self.assertEqual(response['srcDatum'], 'NAD83(2011)')
        self.assertEqual(response['destDatum'], 'NAD83(NSRS2007)')


if __name__ == '__main__':
    unittest.main()
