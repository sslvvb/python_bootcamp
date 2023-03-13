import unittest

from ex00 import add_ingot
from ex00 import get_ingot
from ex00 import empty


class TestPurse(unittest.TestCase):

    def test_purse_1(self):
        dictionary: dict[str, int] = {}
        self.assertEqual(add_ingot(get_ingot(add_ingot(empty(dictionary)))), {'gold_ingots': 1})



    # def test_purse_2(self):
    #     temp: dict[str, int] = {"4": 88}
    #     temp = empty(temp)
    #     temp = add_ingot(temp)
    #     self.assertEqual(temp, {'gold_ingots': 1})
    #
    # def test_purse_3(self):
    #     temp: dict[int, int] = {99: 88}
    #     with self.assertRaises(Exception):
    #         empty(temp)

class ejrhejh()

if __name__ == '__main__':
    unittest.main()
