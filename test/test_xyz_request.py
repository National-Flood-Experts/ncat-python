import unittest
from src.ncatapi import NCAT
from src.Exceptions import RequiredParameterMissingException


class xyzRequestTests(unittest.TestCase):
    def test_it_should_raise_an_exception_if_required_parameters_are_missing_from_a_xyz_request(self):
        ncat = NCAT()
        try:
            ncat.xyz({
                'x': -217687.279,
                'z': 3852223.048,
                'inDatum': 'NAD83(2011)',
                'outDatum': 'NAD83(NSRS2007)'
            })
            self.fail('Failed to assert that the RequiredParameterMissingException was raised.')
        except RequiredParameterMissingException:
            self.assertRaises(RequiredParameterMissingException)
        except Exception as error:
            message = 'Wrong exception was raised: ' + type(error).__name__
            self.fail(message)

    def test_it_should_make_a_xyz_request_if_all_of_the_required_parameters_are_included(self):
        ncat = NCAT()
        response = ncat.xyz({
            'x': -217687.279,
            'y': -5069012.406,
            'z': 3852223.048,
            'inDatum': 'NAD83(2011)',
            'outDatum': 'NAD83(NSRS2007)'
        })
        self.assertEqual(response['x'], '-217,687.297')
        self.assertEqual(response['y'], '-5,069,012.421')
        self.assertEqual(response['z'], '3,852,223.063')


if __name__ == '__main__':
    unittest.main()
