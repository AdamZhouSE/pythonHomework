t = int(input())
result = []
for i in range(t):
    n = int(input())
    tmp = [x for x in range(1, n + 1) if bin(x).count('00') == 0 and bin(x).count('11') == 0]
    result.append(tmp)
for i in result:
    print(*i)
