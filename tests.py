import unittest
import vector_math
from data import *
from vector_math import *
from collisions import *
from cast import *
from commandline import *
from ray_caster import *

class TestCases(unittest.TestCase):
    def test_readFile(self):
        self.assertEqual(readFile())


if __name__ == '__main__':
    unittest.main()
