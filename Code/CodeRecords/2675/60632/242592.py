t = int(input())
result = []
for i in range(t):
    n = int(input())
    r = int(str(n).replace('6','9'))
    result.append(r-n)
for i in result:
    print(i)
