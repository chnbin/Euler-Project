'''
Largest prime factor
Problem 3 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math

def LargestPrimeFactor(n):
    maxPrime = -1

    while n % 2 == 0:
      maxPrime = 2
      n = n / 2
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
      if n % i == 0:
        maxPrime = i
        n = n / i
    
    if n > 2:
      maxPrime = n
    
    return maxPrime

print(LargestPrimeFactor(600851475143))