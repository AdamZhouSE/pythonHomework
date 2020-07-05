def find(n):
    if n == 1 or n == 2:
        return 1
    else:
        if n % 2 == 0:
            return 1 + find(n-1)
        else:
            return find(n-1)


k = int(input())
print(find(k))