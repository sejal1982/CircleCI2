import unittest
from main import to_upper     # Main.py




class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "Kajal"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, "Kajal")




if __name__ == '__main__':
    unittest.main()
