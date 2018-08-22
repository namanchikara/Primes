def isprime(n):
    """ Python program to check whether a number is prime or not """
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def slowIsPrime(n):
    """Slow, But would work around almost all test cases """
        if n<0:
            return False    
        elif n==1:
            False
        else:
            flag = 0
            if n%2 == 0 and n!=2:
                flag = 1
            
            else:
                for i in range(3, int(n**(1/2))+1, 2):
                    if n%i ==0:
                        flag = 1
                        break

            if flag == 0:
                True
            else:
                False
