num = int(input())
n = {}
for i in range(num):
    n[i] = list(map(int, input().split()))
tmp = 0
for j in range(num-1):
    if n[j][1] <= n[j+1][1]:
        tmp = n[j][0]*n[j][1] + n[j+1][0]*n[j+1][1]
        j = j + 1
    else:
        if j == num-1:
            tmp = n[j][0]*n[j][1] + n[j+1][0]*n[j+1][1]
        else:
            tmp = n[j][0] * n[j][1]
