def get(n):
    if n > 10:
        return get(10)
    elif n == 1:
        return 10
    elif n == 2:
        return 91
    else:
        result = 9
        i = 1
        while i < n:
            result *= 10-i
            i += 1
        return result + get(n-1)



n = int(input())
print(get(n))
