t = int(input())
result = []
for i in range(t):
    n, m = map(int, input().split(' '))
    a = list(set(list(map(int, input().split(' ')))))
    b = list(set(list(map(int, input().split(' ')))))
    count = 0
    for j in a:
        if j in b:
            count += 1
    result.append(count)
for i in result:
    print(i)
