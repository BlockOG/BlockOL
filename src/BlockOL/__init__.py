def is_prime(n: int) -> bool:
    """Returns whether n is a prime number
    
    Args:
        n (int): The number to check
    
    Returns:
        bool: Whether n is a prime number
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prev_prime(n: int) -> int:
    """Returns the previous prime number before n
    
    Args:
        n (int): The number to find the previous prime of
    
    Returns:
        int: The previous prime number before n
    """
    if n <= 1: return 2
    n -= 1
    while not is_prime(n):
        n -= 1
        if n < 2: return None
    return n

def next_prime(n: int) -> int:
    """Returns the next prime number after n
    
    Args:
        n (int): The number to find the next prime of
    
    Returns:
        int: The next prime number after n
    """
    n += 1
    while not is_prime(n):
        n += 1
    return n

def fibn(endn: int) -> list:
    """Given an end number, returns the fibonacci numbers up to that number
    
    Args:
        endi (int): The end number
    
    Returns:
        list: The fibonacci numbers up to that number
    """
    fibs = [0, 1]
    while fibs[-1] < endn:
        fibs.append(fibs[-2] + fibs[-1])
    return fibs[:-1]

def fibi(endi: int) -> list:
    """Given an end number, returns the number fibonacci numbers up to that number
    
    Args:
        endn (int): The end number
    
    Returns:
        list: The fibonacci numbers up to that number
    """
    fibs = [0, 1]
    for _ in range(endi - 2):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs

def fib():
    """Returns the fibonacci numbers generator
    
    Yields:
        int: The next fibonacci number
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def zeros_after(n: int) -> int:
    """Counts the number of trailing zeros in n
    
    Args:
        n (int): The number to count the zeros of
    
    Returns:
        int: The number of trailing zeros in n
    """
    zeros = 0
    for i in str(n)[::-1]:
        if i != "0": break
        zeros += 1
    
    return zeros

def counter(dic: dict, ns: iter) -> dict:
    """Counts the number of times each element in ns appears and adds it to dic
    
    Args:
        dic (dict): The dictionary to add the counts to
        ns (iter): The iterable to count the elements of
    
    Returns:
        dict: The dictionary with the counts added
    """
    for n in ns:
        dic[n] = dic.get(n, 0) + 1
    
    return dic

def diviz(n: int) -> list:
    """Returns all the numbers that divide n
    
    Args:
        n (int): The number to divide
    
    Returns:
        list: The numbers that divide n
    """
    if is_prime(n): return [1, n]
    if n in (0, 1): return [1] * n
    a = [1]
    
    for i in range(2, n - 1):
        if n % i == 0:
            a.append(i)
    
    return a + [n]

def diviz_fl(n: int) -> list:
    """Returns the first and last numbers that divide n
    
    Args:
        n (int): The number to divide
    
    Returns:
        list: The first and last numbers that divide n
    """
    if is_prime(n) or n in (0, 1):
        return [1, n]
    
    for i in range(2, n - 1):
        if n % i == 0:
            return [i, int(n / i)]

def largest_prime_div(n):
    """Returns the largest prime divisor of n
    
    Args:
        n (int): The number to divide
    
    Returns:
        int: The largest prime divisor of n
    """
    i = 2
    
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    
    return n

def prime_div(n):
    """Returns the prime divisors of n
    
    Args:
        n (int): The number to divide
    
    Returns:
        list: The prime divisors of n
    """
    i = 2
    factors = []
    
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    
    if n > 1:
        factors.append(n)
    
    return factors
