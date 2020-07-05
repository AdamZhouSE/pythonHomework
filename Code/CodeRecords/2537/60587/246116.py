inp = input().split(',')
n = int(input())
num = len(inp)

res = inp[0]
for i in range(0, num):
    tmp = 0
    for j in range(0, num):
        if inp[i] <= inp[j]:
            tmp += 1
    if tmp == n:
        res = inp[i]
        break
print(res)
