t = int(input())
result = []
for i in range(t):
    a, b = map(str, input().split(' '))
    result.append(len(set(list(a+b))))
for i in result:
    print(i)
