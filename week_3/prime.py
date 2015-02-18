__author__ = 'student'
import math


def is_prime(num):
    numbers = range(2, num)
    for number in numbers:
        # check if prime
        divisors = range(2, number)
        for divisor in divisors:
            if number % divisor == 0 and divisor != number:
                print "not a prime"
            elif number % divisor == 0 and divisor == number:
                print number

# is_prime(7)


def is_prime(number):
    limit = range(1, number)
    # [1, 2, 3]
    for i in limit:
        divide_by = range(1, i)
        for j in divide_by:
            if i % j == 0:
                print("%d is not prime" % i)
        else:
            print("%d is prime" % i)


def loop_through_stuff_up_to_root(number):
    limit = math.sqrt(number)
    limit = math.floor(limit)
    limit = int(limit)
    for i in range(3, limit):
        is_prime(i)

loop_through_stuff_up_to_root(81)