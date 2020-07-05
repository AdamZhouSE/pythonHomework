def ugly_num(n, primes):
    ptr = 0
    ptrs = [0] * len(primes)
    uglys = [0] * len(primes)
    result_ugly = [0] * n
    result_ugly[0] = 1
    while ptr < n - 1:
        i = 0
        while i < len(primes):
            uglys[i] = int(result_ugly[ptr] / primes[i]) + 1
            temporary_ptr = ptrs[i]
            while result_ugly[temporary_ptr] < uglys[i]:
                temporary_ptr += 1
            uglys[i] = primes[i] * result_ugly[temporary_ptr]
            ptrs[i] = temporary_ptr
            i += 1
        ptr += 1
        result_ugly[ptr] = min([i for i in uglys])
    return result_ugly[ptr]


print(ugly_num(int(input()), [int(i) for i in input().split(',')]))