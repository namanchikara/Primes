def isprime(n):
    """ Python program to check whether a number is prime or not """
    if n == 2:
        return 'Prime'
    if n == 3:
        return 'Prime'
    if n % 2 == 0:
        return 'Not prime'
    if n % 3 == 0:
        return 'Not prime'

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return 'Not prime'

        i += w
        w = 6 - w

    return 'Prime'
