def is_prime(number):
    """
    Checks if a given number is a prime number.
    A prime number is a natural number greater than 1 that has no positive 
    divisors other than 1 and itself.
    """
    # Numbers less than or equal to 1 are not prime
    if number <= 1:
        return False
    
    # Check for factors from 2 up to the square root of the number
    # We only need to check up to the square root for efficiency
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            # If a factor is found, it's not prime
            return False
            
    # If no factors are found, the number is prime
    return True

# --- Example Usage ---

# Test with a prime number (e.g., 29)
num_to_check_1 = 29
if is_prime(num_to_check_1):
    print(f"{num_to_check_1} is a prime number.")
else:
    print(f"{num_to_check_1} is not a prime number.")

# Test with a non-prime number (e.g., 15)
num_to_check_2 = 15
if is_prime(num_to_check_2):
    print(f"{num_to_check_2} is a prime number.")
else:
    print(f"{num_to_check_2} is not a prime number.")

# Test with a boundary case (e.g., 1)
num_to_check_3 = 1
if is_prime(num_to_check_3):
    print(f"{num_to_check_3} is a prime number.")
else:
    print(f"{num_to_check_3} is not a prime number.")
