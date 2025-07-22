import unittest
import add_integer

class AddTestCase(unittest.TestCase):
    """ Unittests fr the add_integer()"""

    def test_add_two_integers(self):
        self.assertEqual(add_integer.add_integer(10, 20), 30)
        self.assertEqual(add_integer.add_integer(10, -10), 0)
        self.assertEqual(add_integer.add_integer(5, 10.0), 15)


    def test_raises_type_error(self):
        with self.assertRaises(TypeError):
            add_integer.add_integer("str" , "str")



if __name__ == "__main__":
    unittest.main()

