t = int(input())
result = []
for i in range(t):
    n = int(input())
    a = list(input())
    result.append(-1)
    for j in a:
        if a.count(j) == 1:
            result.pop()
            result.append(j)
            break
for i in result:
    print(i)
