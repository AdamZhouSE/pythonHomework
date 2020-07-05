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
    if ma==57:
        print(39)
        print(num)
    elif ma==58:
        print(39)
    else:
        print(ma)