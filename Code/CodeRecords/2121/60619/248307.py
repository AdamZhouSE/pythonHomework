def get(n):
    if n > 10:
        return get(10)
    else:
        result = 1
        i = 0
        while i < n:
            result *= 10-i
            i += 1
        return result+1



n = int(input())
print(get(n))
