"""
Problem 12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
import math
def triangle_numbers():
    """
    Generates triangular numbers and finds number of its divisors
    """
    
    n = 10
    limit = 500
    
    while True:
        # nth triangular number is given by the formula below
        n_triangle = n * (n + 1) / 2
        
        # Count for number of divisors 
        count = 0
        
        # Finding number of divisors
        for i in range(1, int(math.floor(math.sqrt(n_triangle)))):
            if n_triangle % i == 0:
                count = count + 1
        # Since each count gives 2 divisors i and n/i, we use limit/2
        if count >= limit/2:
            ans = n_triangle
            break
        
        n = n + 1
    
    return ans

print "Answer by traditional method: ", triangle_numbers()
