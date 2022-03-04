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
        if n < 0: return None
    return n

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

def fibonacci(end):
    fibs = [1, 1]
    while fibs[-1] < end:
        fibs.append(fibs[-2] + fibs[-1])
    return fibs

def zeros_afer(n):
    a = 0
    
    for i in str(n)[::-1]:
        if i != "0":
            break
        a += 1
    
    return a

def counter(dic, ns):
    for n in ns:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
    
    return dic

def diviz(n, start=2):
    if is_prime(n):
        return [1, n]
    if n in (0, 1):
        return [1] * n
    
    start = abs(start)
    
    for i in range(start, n - 1):
        if n % i == 0:
            return [i, int(n / i)]

def prime_div(n):
    a = {}
    b = 2
    _f = zeros_afer(n)
    
    if _f > 0 and n != 0:
        n = int(n / pow(10, _f))
        a = {2: _f, 5: _f}
    
    e = diviz(n, b)
    while e[0] > 1:
        n = e[1]
        a = counter(a, [e[0]])
        b = e[0]
        e = diviz(n, b)
    
    if n and n - 1:
        a = counter(a, [n])
    
    return a
