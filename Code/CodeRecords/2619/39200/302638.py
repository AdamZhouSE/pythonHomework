def func(n):
    multi = []
    for i in range(len(n)):
        count = 1
        for j in range(i, len(n)):
            count *= int(n[j])
            if count in multi:
                return 0
            else:
                multi.append(count)
    return 1


t = int(input())
for x in range(t):
    print(func(input()))
