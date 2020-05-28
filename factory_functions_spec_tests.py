import unittest
from factory_functions import *
# define the tests before we code the functions

class TestFactoryFunctions(unittest.TestCase):
    # TEST 1
    def test_make_dough(self):
        self.assertEqual(make_dough('water', 'flour'), 'dough')
        self.assertEqual(make_dough('water', 'cheese'), 'not dough')


if __name__ == '__main__':
    unittest.main()
