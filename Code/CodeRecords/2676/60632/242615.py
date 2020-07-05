t = int(input())
result = []
for i in range(t):
    n, k = map(int, input().split(' '))
    data = list(map(int, input().split(' ')))
    maxi = 0
    for j in range(0, n - k + 1):
        if sum(data[j:j + k]) > maxi:
            maxi = sum(data[j:j + k])
    result.append(maxi)
for i in result:
    print(i)
