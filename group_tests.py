import unittest

from group import groups_of_3


class MyTestCase(unittest.TestCase):

    def test_groups_of_3(self):
        array = [1,2,3,4,5,6,7,8,9]
        expected = [[1,2,3],[4,5,6],[7,8,9]]
        result = groups_of_3(array)
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main()
