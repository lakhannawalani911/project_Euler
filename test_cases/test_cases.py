import unittest
from euler_problem.problem_1 import multiplesof3and5
from euler_problem.problem_2 import fiboEvenSum
from euler_problem.problem_3 import largestPrimeFactor

class TestCases(unittest.TestCase):

    def test_problem1(self):
        self.assertEqual(multiplesof3and5(10), 23)
        self.assertEqual(multiplesof3and5(49), 543)
        self.assertEqual(multiplesof3and5(1000), 233168)
        self.assertEqual(multiplesof3and5(8456), 16687353)
        self.assertEqual(multiplesof3and5(19564), 89301183)

    def test_problem2(self):
        self.assertEqual(fiboEvenSum(10), 10)
        self.assertEqual(fiboEvenSum(34), 44)

    def test_problem3(self):
        self.assertEqual(largestPrimeFactor(2), 2)
        self.assertEqual(largestPrimeFactor(3), 3)
        self.assertEqual(largestPrimeFactor(5), 5)
        self.assertEqual(largestPrimeFactor(7), 7)
        self.assertEqual(largestPrimeFactor(8), 2)
        self.assertEqual(largestPrimeFactor(13195), 29)

if __name__ == "__main__":
    unittest.main()