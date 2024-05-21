
# This module is used for timing operations. 
# Here it's used to calculate the time taken by each method to generate prime numbers.
import time 

# This module provides access to some variables used or maintained by the Python interpreter. 
# Here it's used to read command-line arguments and to handle early exits. 
import sys

# This module is used to generate random numbers. 
# Here it's used in the Miller-Rabin method to generate a random number.
import random


"""
This function finds prime numbers in a range using the brute force method. 
It checks each number one by one to see if it has any factors other than 1 and itself. 
If a number has no other factors, it's prime. This method is simple but slow, especially for large ranges, 
because it checks every single number.
"""
# This function finds prime numbers in a range using the brute force method.
def brute_force_method(start, end):
    # We start by making a list to keep track of the prime numbers we find.
    primes = []
    
    # We look at each number in the range one by one.
    for num in range(start, end + 1):
        # Numbers less than or equal to 1 are not prime, so we skip them.
        if num <= 1:
            continue
        
        # We check if 'num' has any factors other than 1 and itself.
        # We only need to check up to the square root of 'num', because a larger factor would have a corresponding smaller factor.
        for i in range(2, int(num**0.5) + 1):
            # If 'num' is divisible by 'i', then it's not prime, so we break the loop and move on to the next number.
            if num % i == 0:
                break
        else:
            # If we didn't find any factors, then 'num' is prime, so we add it to our list.
            primes.append(num)
    
    # We return our list of prime numbers.
    return primes


"""
This function finds prime numbers in a range using the trial division method. 
It improves on the brute force method by skipping even numbers and multiples of 3. 
It checks each remaining number to see if it has any factors other than 1 and itself. 
If a number has no other factors, it's prime. This method is faster than the brute force method, 
but still relatively slow for large ranges.
"""
# This function finds prime numbers in a range using the trial division method.
def trial_division_method(start, end):
    # We start by making a list to keep track of the prime numbers we find.
    primes = []
    
    # We look at each number in the range one by one.
    for num in range(start, end + 1):
        # Numbers less than or equal to 1 are not prime, so we skip them.
        if num <= 1:
            continue
        
        # The numbers 2 and 3 are prime, so if we see them, we add them to our list.
        if num <= 3:
            primes.append(num)
            continue
        
        # Even numbers and multiples of 3 are not prime, so we skip them.
        if num % 2 == 0 or num % 3 == 0:
            continue
        
        # We check if 'num' has any factors other than 1 and itself.
        # We start from 5 and increment by 6 each time, because all primes are of the form 6n±1, except for 2 and 3.
        i = 5
        while i * i <= num:
            # If 'num' is divisible by 'i' or 'i+2', then it's not prime, so we break the loop and move on to the next number.
            if num % i == 0 or num % (i + 2) == 0:
                break
            i += 6
        else:
            # If we didn't find any factors, then 'num' is prime, so we add it to our list.
            primes.append(num)
    
    # We return our list of prime numbers.
    return primes

"""
This function finds prime numbers in a range using the Miller-Rabin method. 
This is a probabilistic test that's much faster for large numbers. 
It picks a random number 'a' and checks if it satisfies certain conditions. If 'a' does, 
then the number is probably prime. If 'a' doesn't, then the number is composite. 
The more random numbers 'a' we check, the more confident we can be in the result. 
However, this method might occasionally guess wrong.
"""
# This function finds prime numbers in a range using the Miller-Rabin method.
def miller_rabin_method(start, end, k=5):
    # We start by making a list to keep track of the prime numbers we find.
    primes = []
    
    # We look at each number in the range one by one.
    for num in range(start, end + 1):
        # Numbers less than or equal to 1 are not prime, so we skip them.
        if num <= 1:
            continue
        
        # The numbers 2 and 3 are prime, so if we see them, we add them to our list.
        if num <= 3:
            primes.append(num)
            continue
        
        # Even numbers and multiples of 3 are not prime, so we skip them.
        if num % 2 == 0 or num % 3 == 0:
            continue
        
        # We write (num-1) as a product of a power of 2 (s) and an odd number (d).
        # This is because we want to use the property that for any prime number p and any number a, a^(p-1) is congruent to 1 modulo p.
        d = num - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        
        # We do a loop 'k' times. Each time, we pick a random number and do some calculations.
        for _ in range(k):
            # Pick a random number 'a' between 2 and 'num' - 2.
            a = random.randint(2, num - 2)
            
            # Compute a^d mod num. This is the first step in checking the property a^(p-1) ≡ 1 (mod p).
            x = pow(a, d, num)
            
            # If 'x' is 1 or 'num' - 1, then 'a' is not a witness for compositeness, so we continue to the next iteration.
            if x == 1 or x == num - 1:
                continue
            
            # Repeat 's' - 1 times.
            for _ in range(s - 1):
                # Square 'x' and reduce modulo 'num'.
                x = pow(x, 2, num)
                
                # If 'x' becomes 'num' - 1, then 'a' is not a witness for compositeness, so we break the loop.
                if x == num - 1:
                    break
            else:
                # If the loop didn't break early, then 'a' is a witness for compositeness, so 'num' is composite and we break the loop.
                break
        else:
            # If none of the 'k' loops found that 'num' is composite, then 'num' is probably prime.
            primes.append(num)
    
    # We return our list of prime numbers.
    return primes

"""
This function finds prime numbers in a range using the Sieve of Eratosthenes method. 
It starts by assuming all numbers are prime, then progressively marks the multiples of each number as composite (not prime). 
At the end, the numbers that are still marked as prime are the prime numbers. This method is very fast and always correct, 
but it needs to make a list of all the numbers up front, which can use a lot of memory for large ranges.
"""
# This function finds prime numbers in a range using the Sieve of Eratosthenes method.
def sieve_of_eratosthenes_method(start, end):
    # We start by making a list of boolean values representing whether each number is prime.
    # We mark 0 and 1 as not prime (False), and all other numbers as prime (True).
    prime = [False, False] + [True] * (end - 1)
    
    # We start checking from the number 2.
    p = 2
    
    # We only need to check numbers up to the square root of 'end'.
    # This is because if 'end' has a factor greater than its square root, it must also have a smaller factor that has already been checked.
    while p * p <= end:
        # If 'p' is marked as prime...
        if prime[p]:
            # ...then we mark all multiples of 'p' as not prime.
            # This is because any multiple of 'p' must have 'p' as a factor, so it can't be prime.
            for i in range(p * p, end + 1, p):
                prime[i] = False
        
        # Move on to the next number.
        p += 1
    
    # At the end, we make a list of all numbers marked as prime in the range from 'start' to 'end'.
    primes = [num for num in range(start, end + 1) if prime[num]]
    
    # We return our list of prime numbers.
    return primes

# This is the main function that runs when the script is executed.
def main():
    # Check if the correct number of arguments are provided. If not, print an error message and exit.
    if len(sys.argv) < 4:
        print("Error: Please provide complete arguments.\nFormat should be : python prime_no_generator.py method_name start end!")
        sys.exit(1)
    
    # Extract the method name, start, and end from the command line arguments.
    method = sys.argv[1] 
    start = int(sys.argv[2])
    end = int(sys.argv[3])

    # Check if the method name is valid. If not, print an error message and exit.
    if method not in ["brute_force", "trial_division", "miller_rabin", "sieve_of_eratosthenes"]:
        print("Error: Invalid method. Choose from 'brute_force', 'trial_division', 'miller_rabin', 'sieve_of_eratosthenes'")
        sys.exit(1)
    
    # Check if the start is less than or equal to the end. If not, print an error message and exit.
    if start > end:
        print("Error! Starting limit cannot be greater than ending limit!")
        sys.exit(1)
    
    # Record the start time before running the prime number generation.
    start_time = time.time()
    
    # Call the appropriate function based on the method name.
    if method == "brute_force":
        prime_no = brute_force_method(start, end)
    elif method == "trial_division":
        prime_no = trial_division_method(start, end)
    elif method == "miller_rabin":
        prime_no = miller_rabin_method(start, end)
    elif method == "sieve_of_eratosthenes":
        prime_no = sieve_of_eratosthenes_method(start, end)
    
    # Record the end time after running the prime number generation.
    end_time = time.time()

    # Print the prime numbers and the time taken.
    print(f"Prime numbers between {start} and {end} using {method} method:")
    print(prime_no)
    print(f"Time taken: {end_time - start_time:.6f} seconds")

# This line checks if the script is being run directly (not being imported as a module). If so, it calls the main function.
if __name__ == "__main__":
    main()


"""
Summary:
This Python script is designed to generate prime numbers within a specified range using four different methods: 
brute force, trial division, Miller-Rabin, and Sieve of Eratosthenes. Each method has its own function defined within the script. 
The script takes command-line arguments to determine the method and the range (start and end) for prime number generation. 
It also measures the time taken by each method to complete the task.

The 'brute_force_method' checks each number for factors up to its square root. The 'trial_division_method' improves efficiency 
by checking divisibility only by 2, 3, and numbers of the form 6n±1. The 'miller_rabin_method' is a probabilistic test that 
uses random numbers to determine primality, particularly useful for large numbers. Lastly, the 'sieve_of_eratosthenes_method' 
efficiently finds all primes in the range by iteratively marking the multiples of each prime number starting from 2.

The 'main' function orchestrates the script's execution: it validates the input arguments, selects the appropriate 
prime-finding method, and prints the results along with the execution time. If the script is run directly, the 'main' 
function is called, ensuring that the script can also be imported as a module without immediately executing.
"""