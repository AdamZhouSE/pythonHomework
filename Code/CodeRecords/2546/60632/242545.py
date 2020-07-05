def padovan(x):
    if x == 0 or x == 1 or x == 2:
        return 1
    else:
        return padovan(x-2) + padovan(x-3)


t = int(input())
result = []
for i in range(t):
    n = int(input())
    result.append(padovan(n))
for i in result:
    print(i)
