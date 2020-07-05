n, p = map(int, input().split(' '))
num = [int(i) for i in input().split(' ')]
m = int(input())
for step in range(m):
    temp = [int(i) for i in input().split(' ')]
    if temp[0] == 1:
        for i in range(temp[1] - 1, temp[2]):
            num[i] *= temp[3]
    elif temp[0] == 2:
        for i in range(temp[1] - 1, temp[2]):
            num[i] += temp[3]
    else:
        print(sum(num[temp[1] - 1:temp[2]]) % p)