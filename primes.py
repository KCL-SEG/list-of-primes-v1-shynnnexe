"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(num):
    for i in range(2, int(num**0.5)+1): #start counting from 2; number we are counting to is the sqrt of the number we are checking
        if num % 1 == 0: #for each num, check if divisible (evenly) by counting number
            return False #not prime
    return True #prime

def primes(number_of_primes):
    list = []
    num = 2 #first prime number
    return list
    
    while len(list) < number_of_primes: #loop continues
        if isPrime(num): #for each number, ask if prime
            list.append(num) #if prime, number gets added to list
        num += 1 #move on to next number to repeat process
    return list