# Import unittest library and function being tested
import unittest
from levenshtein_distance import levenshtein_distance as ld

class Tests(unittest.TestCase):
    def test_1(self):
        """Check both null strings"""
        self.assertEqual(ld("", ""), 0)

    def test_2(self):
        """Check null first string"""
        self.assertEqual(ld("", "a"), 1)

    def test_3(self):
        """Check null second string"""
        self.assertEqual(ld("a", ""), 1)

    def test_4(self):
        """Check dog -> cat"""
        self.assertEqual(ld("dog", "cat"), 3)

    def test_5(self):
        """Check cog -> cat"""
        self.assertEqual(ld("cog", "cat"), 2)

    def test_6(self):
        """Check car -> racecar"""
        self.assertEqual(ld("car", "racecar"), 4)

    def test_7(self):
        """Check race -> racecar"""
        self.assertEqual(ld("race", "racecar"), 3)

    def test_8(self):
        """Check dog -> dog"""
        self.assertEqual(ld("dog", "dog"), 0)

if __name__ == "__main__":
    unittest.main()