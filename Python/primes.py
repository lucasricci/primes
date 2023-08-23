"""
Simple program to calculate how many prime numbers are in a range.
22/08/23 - Lucas Ricci

Heavily inspired by: https://github.com/PlummersSoftwareLLC/Primes/tree/drag-race/PrimePython
"""
import timeit
import numpy as np
from math import sqrt


def eratosthenes_sieve(n):
    primes = np.ones(limit, dtype=bool)
    primes[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            primes[i * i :: i] = False
    return np.nonzero(primes)[0]


passes = 0
limit = 10**6
count = len(eratosthenes_sieve(limit))

prime_counts = {
    10: 4,
    100: 25,
    1000: 168,
    10000: 1229,
    100000: 9592,
    1000000: 78498,
    10000000: 664579,
    100000000: 5761455,
}


time_start = timeit.default_timer()

while timeit.default_timer() - time_start < 5:
    eratosthenes_sieve(limit)
    passes += 1

time_delta = timeit.default_timer() - time_start

if count == prime_counts[limit]:
    validity = True

print(
    f"Count = {count}; Pass = {passes}; Validity = {validity}; Time = {time_delta}; Average = {passes/time_delta}"
)
