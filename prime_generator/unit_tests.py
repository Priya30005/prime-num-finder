# Import the unittest module. This is a built-in Python module for writing and running tests.
import unittest

# Import the prime number generation functions from the 'prime_no_generator' module.
from prime_no_generator import brute_force_method, trial_division_method, miller_rabin_method, sieve_of_eratosthenes_method

# Define a test case class that inherits from unittest.TestCase. Each method in this class is a separate test.
class TestPrimeMethods(unittest.TestCase):

    # Test the brute force method with two different ranges.
    def test_brute_force_method(self):
        # Check that the function returns the correct prime numbers for the range 1-10.
        self.assertEqual(brute_force_method(1, 10), [2, 3, 5, 7])
        # Check that the function returns the correct prime numbers for the range 10-30.
        self.assertEqual(brute_force_method(10, 30), [11, 13, 17, 19, 23, 29])

    # Test the trial division method with two different ranges.
    def test_trial_division_method(self):
        # Check that the function returns the correct prime numbers for the range 1-20.
        self.assertEqual(trial_division_method(1, 20), [2, 3, 5, 7, 11, 13, 17, 19])
        # Check that the function returns the correct prime numbers for the range 20-40.
        self.assertEqual(trial_division_method(20, 40), [23, 29, 31, 37])

    # Test the Miller-Rabin method with two different ranges.
    def test_miller_rabin_method(self):
        # Check that the function returns the correct prime numbers for the range 1-30.
        self.assertEqual(miller_rabin_method(1, 30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        # Check that the function returns the correct prime numbers for the range 30-50.
        self.assertEqual(miller_rabin_method(30, 50), [31, 37, 41, 43, 47])

    # Test the Sieve of Eratosthenes method with two different ranges.
    def test_sieve_of_eratosthenes_method(self):
        # Check that the function returns the correct prime numbers for the range 1-40.
        self.assertEqual(sieve_of_eratosthenes_method(1, 40), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
        # Check that the function returns the correct prime numbers for the range 40-60.
        self.assertEqual(sieve_of_eratosthenes_method(40, 60), [41, 43, 47, 53, 59])

# This line checks if the script is being run directly (not being imported as a module). If so, it runs the tests.
if __name__ == '__main__':
    unittest.main()

"""
This Python script is a unit test for various prime number generation methods. 
The methods being tested are imported from a module named 'prime_no_generator'. The methods include:

1. `brute_force_method`: This method generates prime numbers in a given range using a brute force approach. 
It checks each number in the range to see if it has any divisors other than 1 and itself.

2. `trial_division_method`: This method also generates prime numbers in a given range. It improves upon 
the brute force method by only checking divisibility up to the square root of the number.

3. `miller_rabin_method`: This method uses the probabilistic Miller-Rabin primality test to generate prime 
numbers in a given range. It is faster and more efficient for larger ranges.

4. `sieve_of_eratosthenes_method`: This method generates prime numbers in a given range using the Sieve of Eratosthenes 
algorithm, which is an efficient way to find all primes smaller than a given limit.

Each method is tested with two different ranges of numbers. The expected output for each test is a list of prime numbers 
in the given range. The tests ensure that each method is correctly identifying prime numbers.

The script uses Python's built-in `unittest` module to run the tests. 

The script uses Python's built-in `unittest` module to run the tests. 
The `self.assertEqual` function is used to compare the output of each method with the expected result. 
If the two values are not equal, the function raises an `AssertionError`, indicating that the test has failed.

If the script is run as the main program, it will execute all the tests and report the results.
"""