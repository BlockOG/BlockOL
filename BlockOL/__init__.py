"""A utils library."""

from typing import Any, Generator, Union, Iterable, Tuple, List, Dict, Callable


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
    while i**2 <= n:
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
    if n <= 1:
        return 2
    n -= 1
    while not is_prime(n):
        n -= 1
        if n < 2:
            return None
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


def nth_prime(n: int) -> int:
    """Returns the nth prime number

    Args:
        n (int): Which prime number to find

    Returns:
        int: The nth prime number
    """
    primes = [2]
    i = 3

    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 2

    return primes[-1]


def fibn(endn: int) -> List[int]:
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


def fibi(endi: int) -> List[int]:
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


def fib() -> Generator[int, None, None]:
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
        if i != "0":
            break
        zeros += 1

    return zeros


def counter(dic: Dict, ns: Iterable) -> Dict:
    """Counts the number of times each element in ns appears and adds it to dic

    Args:
        dic (dict): The dictionary to add the counts to
        ns (iterable): The elements to count

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
    if is_prime(n):
        return [1, n]
    if n in (0, 1):
        return [1] * n
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


def largest_prime_div(n: int) -> int:
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


def prime_div(n: int) -> list:
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


def bin_search_min(func: Callable) -> int:
    """Finds the minimum value where the function returns True

    Args:
        func (Callable): The function to test

    Returns:
        int: The minimum value where the function returns True
    """

    i, j = -10, -10
    while func(i):
        i *= 10
    i //= 10
    j = i
    while j != 0:
        if func(i):
            i += j
        else:
            i -= j
            j = -(-j // 10)
    return i


def bin_search(func: Callable, mi: int, ma: int) -> int:
    """Find the value where the function returns 0. The function should return -1 if the value is too low, 1 if the value is too high, and 0 if the value is correct.

    Args:
        func (Callable): The function to test
        mi (int): The minimum value to test
        ma (int): The maximum value to test

    Returns:
        int: The value where the function returns 0
    """

    pi = i = (mi + ma) // 2
    while True:
        if (j := func(i)) == -1:
            mi = i - 1
            pi, i = i, (ma + i) // 2
            if pi == i:
                raise ValueError("Value not found in given range")
        elif j == 0:
            return i
        elif j == 1:
            ma = i + 1
            i = (mi + i) // 2


def bin_search_max(func):
    """Finds the maximum value where the function returns True

    Args:
        func (Callable): The function to test

    Returns:
        int: The maximum value where the function returns True
    """

    i, j = 10, 10
    while func(i):
        i *= 10
    i //= 10
    j = i
    while j != 0:
        if func(i):
            i += j
        else:
            i -= j
            j //= 10
    return i


def teef(
    tr: Callable,
    exces: Union[Tuple[BaseException], BaseException] = (),
    exc: Callable = lambda a, e: None,
    els: Callable = lambda a: None,
    fin: Callable = lambda a: None,
) -> Tuple[Tuple[Any, Any, Any, Any], Dict]:
    """teef: Try Except Else Finally. All functions get called with a dictionary for talking between them.
    And the except function also gets the exception as an argument.

    Args:
        tr (Callable): try function
        exces (Union[Tuple[BaseException], BaseException], optional): Exceptions. Defaults to ().
        exc (Callable, optional): except function. Defaults to lambda a, e: None.
        els (Callable, optional): else function. Defaults to lambda a: None.
        fin (Callable, optional): finally function. Defaults to lambda a: None.

    Returns:
        Tuple[Tuple[Any, Any, Any, Any], Dict]: The results of the functions and the dictionary
    """

    ret = [None, None, None, None]
    gls = {}
    try:
        ret[0] = tr(gls)
    except exces as e:
        ret[1] = exc(gls, e)
    else:
        ret[2] = els(gls)
    finally:
        ret[3] = fin(gls)
    return tuple(ret), gls
