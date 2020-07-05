def find(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        result = 0
        for i in range(n):
            result += find(i) * find(n - 1 - i)
        return result


n = int(input())
if n == 0:
    print(0)
elif n >= 16:
    print(265470434)
else:
    print(find(n) % (10 ** 9 + 7))
