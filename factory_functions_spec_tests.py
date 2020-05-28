import unittest
from factory_functions import *
# define the tests before we code the functions

class TestFactoryFunctions(unittest.TestCase):
    # TEST 1
    def test_make_dough(self):
        self.assertEqual(make_dough('water', 'flour'), 'dough')
        self.assertEqual(make_dough('water', 'cheese'), 'not dough')
        self.assertEqual(make_dough('water', 'wholegrain flour'), 'brown dough')


    def test_make_bread(self):
        self.assertEqual(make_bread('dough'), 'bread')
        self.assertEqual(make_bread('not dough'), 'not bread')
        self.assertEqual(make_bread('brown dough'), 'brown bread')


if __name__ == '__main__':
    unittest.main()
