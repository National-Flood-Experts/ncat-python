import unittest
from src.ncatapi import NCAT
from src.Exceptions import RequiredParameterMissingException


class USNGRequestTests(unittest.TestCase):
    def test_it_should_raise_an_exception_if_required_parameters_are_missing_from_a_USNG_request(self):
        ncat = NCAT()
        try:
            ncat.usng({
                'usng': '15SWB4788338641',
                'outDatum': 'nad83(NSRS2007)'
            })
            self.fail('Failed to assert that the RequiredParameterMissingException was raised.')
        except RequiredParameterMissingException:
            self.assertRaises(RequiredParameterMissingException)
        except Exception as error:
            message = 'Wrong exception was raised: ' + type(error).__name__
            self.fail(message)

    def test_it_should_make_a_USNG_request_if_all_of_the_required_parameters_are_included(self):
        ncat = NCAT()
        response = ncat.usng({
            'usng': '15SWB4788338641',
            'inDatum': 'nad83(2011)',
            'outDatum': 'nad83(NSRS2007)'
        })
        self.assertEqual(response['utmZone'], 'UTM Zone 15')


if __name__ == '__main__':
    unittest.main()
