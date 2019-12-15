#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

# problem50.py
# solution not efficient D: much more 10min to process, i want a solution whose take below 1 minute of time.
"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""

from primes import primeGen

max_n = 10 ** 6


def sumOfPrimes(primes):
    i = 0
    prime = primes[-1]
    rangeTest = prime ** 1/2
    while primes[i] < rangeTest:
        j = i
        sumTemp = 0
        while primes[j] < rangeTest:
            sumTemp += primes[j]
            if sumTemp == prime:
                return prime, abs(j - i) + 1
            j += 1
        i += 1
    return 0, 0


def main(n):
    primes = []
    mostConsecutivePrime, mostSums = 0, 0
    for prime in primeGen(n):
        primes.append(prime)
        prime, sums = sumOfPrimes(primes)
        if mostSums < sums:
            mostConsecutivePrime, mostSums = prime, sums

    print(mostConsecutivePrime)

main(max_n)