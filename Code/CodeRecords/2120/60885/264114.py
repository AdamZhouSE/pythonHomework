def division_and_mul(n):
    if n == 2:
        return 1
    result = 1
    while n > 0:
        if n >= 5:
            result *= 3
            n -= 3
        else:
            if n == 4:
                result *= 4
            else:
                result *= 2
            break      
    return result

n = int(input())
result = division_and_mul(n)
print(result)