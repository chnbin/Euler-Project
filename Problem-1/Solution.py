'''
Multiples of 3 and 5
Problem 1 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def multiples3And5(n):
    sum = 0
    for i in range(1, n):
      if (i % 3 == 0 or i % 5 == 0):
        sum += i

    return sum

def multiples3And5Faster(n):
  count3 = (n - 1) // 3
  count5 = (n - 1) // 5
  count15 = (n - 1) // 15

  return (3 * (1 + count3) * count3 // 2) + (5 * (1 + count5) * count5 // 2) - (15 * (1 + count15) * count15 // 2)

print(multiples3And5(1000000))
print(multiples3And5Faster(1000000))