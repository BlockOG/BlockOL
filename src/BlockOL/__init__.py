def is_prime(n):
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

def prev_prime(n):
    if n <= 1: return 2
    n -= 1
    while not is_prime(n):
        n -= 1
        if n < 2: return None
    return n

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

def fibn(endn):
    fibs = [1, 1]
    while fibs[-1] < endn:
        fibs.append(fibs[-2] + fibs[-1])
    return fibs[:-1]

def fibi(endi):
    fibs = [1, 1]
    for _ in range(endi - 2):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs

def fib():
    a, b = 1, 1
    while True:
        yield a
        c = a + b
        a = b
        b = c

def zeros_after(n):
    a = 0
    
    for i in str(n)[::-1]:
        if i != "0":
            break
        a += 1
    
    return a

def counter(dic, ns):
    for n in ns:
        dic[n] = dic.get(n, 0) + 1
    
    return dic

def diviz(n):
    if is_prime(n): return [1, n]
    if n in (0, 1): return [1] * n
    a = [1]
    
    for i in range(2, n - 1):
        if n % i == 0:
            a.append(i)
    
    return a + [n]

def diviz_fl(n, start=2):
    if is_prime(n) or n in (0, 1):
        return [1, n]
    
    start = abs(start)
    
    for i in range(start, n - 1):
        if n % i == 0:
            return [i, int(n / i)]

def largest_prime_div(n):
    i = 2
    
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    
    return n

def prime_div(n):
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
