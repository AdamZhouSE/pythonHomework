t = int(input())
result = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    tmp = [x for x in a if x % 2 == 0]+[x for x in a if x % 2 == 1]
    result.append(tmp+[''])
for i in result:
    print(*i)
