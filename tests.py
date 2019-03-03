import os
import unittest
from smart_getenv import getenv


class GetenvTests(unittest.TestCase):
    """
    Tests for getenv.
    """

    test_var_name = '__ENV_UTILS_TEST_VAR'

    def setUp(self):
        self.delete_test_var()

    def tearDown(self):
        self.delete_test_var()

    def delete_test_var(self):
        """
        Delete test environment variable.
        """
        if self.test_var_name in os.environ.keys():
            del os.environ[self.test_var_name]

    def test_getenv_default(self):
        """
        If environment variable does not exist:
            ensure getenv returns None if default value is not specified,
            ensure getenv returns default value if it is specified,
            ensure getenv does not cast default value to desired type.
        """
        self.assertEqual(getenv(self.test_var_name), None)
        self.assertEqual(getenv(self.test_var_name, default='default string value'), 'default string value')
        self.assertEqual(getenv(self.test_var_name, type=int, default='default string value'), 'default string value')

    def test_getenv_type_str(self):
        """
        Ensure getenv returns string if environment variable exists and desired type is string.
        """
        os.environ[self.test_var_name] = 'abc'
        self.assertEqual(getenv(self.test_var_name, type=str), 'abc')
        self.assertEqual(getenv(self.test_var_name, default='qwe'), 'abc')

    def test_getenv_type_int(self):
        """
        If environment variable exists and desired type is int:
            ensure getenv returns int,
            ensure getenv excepts if value can not be casted to int.
        """
        os.environ[self.test_var_name] = '123'
        self.assertEqual(getenv(self.test_var_name, type=int), 123)

        os.environ[self.test_var_name] = 'absolutely not an int'
        try:
            getenv(self.test_var_name, type=int)
            self.fail('Calling getenv_int on a environment variable with'
                      ' non-castable to int value should fail with exception!')
        except ValueError:
            pass

        os.environ[self.test_var_name] = '2'
        self.assertEqual(getenv(self.test_var_name, default=1), 2)

    def test_getenv_type_float(self):
        """
        If environment variable exists and desired type is float:
            ensure getenv returns float,
            ensure getenv excepts if value can not be casted to float.
        """
        os.environ[self.test_var_name] = '123.4'
        self.assertEqual(getenv(self.test_var_name, type=float), 123.4)

        os.environ[self.test_var_name] = 'absolutely not a float'
        try:
            getenv(self.test_var_name, type=float)
            self.fail('Calling getenv_int on a environment variable with'
                      ' non-castable to float value should fail with exception!')
        except ValueError:
            pass

        os.environ[self.test_var_name] = '123.4'
        self.assertEqual(getenv(self.test_var_name, default=245.6), 123.4)

    def test_getenv_type_bool(self):
        """
        If environment variable exists and desired type is bool, ensure getenv returns bool.
        """
        os.environ[self.test_var_name] = 'true'
        self.assertEqual(getenv(self.test_var_name, type=bool), True)

        os.environ[self.test_var_name] = 'True'
        self.assertEqual(getenv(self.test_var_name, type=bool), True)

        os.environ[self.test_var_name] = '1'
        self.assertEqual(getenv(self.test_var_name, type=bool), True)

        os.environ[self.test_var_name] = 'absolutely not a boolean'
        self.assertEqual(getenv(self.test_var_name, type=bool), True)

        os.environ[self.test_var_name] = ' '
        self.assertEqual(getenv(self.test_var_name, type=bool), True)

        os.environ[self.test_var_name] = 'false'
        self.assertEqual(getenv(self.test_var_name, type=bool), False)

        os.environ[self.test_var_name] = 'False'
        self.assertEqual(getenv(self.test_var_name, type=bool), False)

        os.environ[self.test_var_name] = '0'
        self.assertEqual(getenv(self.test_var_name, type=bool), False)

        os.environ[self.test_var_name] = ''
        self.assertEqual(getenv(self.test_var_name, type=bool), False)

        os.environ[self.test_var_name] = 'absolutely not a boolean'
        self.assertEqual(getenv(self.test_var_name, default=False), True)

    def test_getenv_type_list(self):
        """
        If environment variable exists and desired type is list:
            ensure getenv returns list,
            ensure getenv default separator is ',',
            ensure getenv supports custom separator.
        """
        os.environ[self.test_var_name] = 'abc'
        self.assertEqual(getenv(self.test_var_name, type=list), ['abc'])

        os.environ[self.test_var_name] = 'a,b,c'
        self.assertEqual(getenv(self.test_var_name, type=list), ['a', 'b', 'c'])

        os.environ[self.test_var_name] = ',a,b,c,'
        self.assertEqual(getenv(self.test_var_name, type=list, separator=','), ['', 'a', 'b', 'c', ''])

        os.environ[self.test_var_name] = 'a:b:c'
        self.assertEqual(getenv(self.test_var_name, type=list, separator=':'), ['a', 'b', 'c'])

        os.environ[self.test_var_name] = 'a,b,c'
        self.assertEqual(getenv(self.test_var_name, default=[1, 2]), ['a', 'b', 'c'])

    def test_getenv_type_tuple(self):
        """
        If environment variable exists and desired type is tuple:
            ensure getenv returns tuple,
            ensure getenv default separator is ',',
            ensure getenv supports custom separator.
        """
        os.environ[self.test_var_name] = 'abc'
        self.assertEqual(getenv(self.test_var_name, type=tuple), ('abc',))

        os.environ[self.test_var_name] = 'a,b,c'
        self.assertEqual(getenv(self.test_var_name, type=tuple), ('a', 'b', 'c'))

        os.environ[self.test_var_name] = ',a,b,c,'
        self.assertEqual(getenv(self.test_var_name, type=tuple, separator=','), ('', 'a', 'b', 'c', ''))

        os.environ[self.test_var_name] = 'a:b:c'
        self.assertEqual(getenv(self.test_var_name, type=tuple, separator=':'), ('a', 'b', 'c'))

        os.environ[self.test_var_name] = 'a,b,c'
        self.assertEqual(getenv(self.test_var_name, default=(1, 2)), ('a', 'b', 'c'))

    def test_getenv_type_dict(self):
        """
        If environment variable exists and desired type is dict:
            ensure getenv returns dict,
            ensure getenv supports custom separator.
        """
        os.environ[self.test_var_name] = '{"key": "value"}'
        self.assertEqual(getenv(self.test_var_name, type=dict), {'key': 'value'})

        os.environ[self.test_var_name] = '{    "key":    "value"      }'
        self.assertEqual(getenv(self.test_var_name, type=dict), {'key': 'value'})

        os.environ[self.test_var_name] = '{    "key":    "value"      }'
        self.assertEqual(getenv(self.test_var_name, type=dict), {'key': 'value'})

        os.environ[self.test_var_name] = 'absolutely not a dict'
        try:
            getenv(self.test_var_name, type=dict)
            self.fail('Calling getenv with desired type of dict on a environment variable with'
                      ' non-castable to dict value should fail with exception!')
        except TypeError:
            pass
        except SyntaxError:
            pass

        os.environ[self.test_var_name] = '{    "key":    "value"      }'
        self.assertEqual(getenv(self.test_var_name, default={"key": "other value"}), {'key': 'value'})


if __name__ == '__main__':
    unittest.main()
