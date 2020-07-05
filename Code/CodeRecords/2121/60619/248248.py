def get(n):
    if n == 2:
        return "12"
    else:
        return get(n - 1) + str(n)


n = int(input())
print(n)
