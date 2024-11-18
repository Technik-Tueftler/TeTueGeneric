import sys
import unittest

sys.path.append('..')


import src

class SrcTestSuite(unittest.TestCase):
    """Src test cases."""
    def test_lala_file(self):
        string = src.lala_file.lala_func()
        self.assertEqual("lala", string)


class GenericTestSuite(unittest.TestCase):
    """Generic test cases."""
    def test_that_riddle_is_solved(self):
        request_timeout = src.REQUEST_TIMEOUT
        self.assertEqual(30, request_timeout)


if __name__ == '__main__':
    unittest.main()
