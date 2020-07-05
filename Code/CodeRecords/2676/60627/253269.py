# 14
n = int(input())
for i in range(n):
    _,k = input().split()
    k = int(k)
    num = input().split()
    for i in range(len(num)):
        num[i] = int(num[i])
    ma = 0
    num.sort(reverse = True)
    for i in range(k):
        ma += num[i]
    print(num,k)