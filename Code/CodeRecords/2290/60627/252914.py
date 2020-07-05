# 1
n = int(input())
for i in range(n):
    input()
    num = input().split()
    for i in range(len(num)):
        num[i] = int(num[i])
    l = ''
    for i in range(len(num)):
        if i < len(num)-1:
            if num[i]  > num[i+1]:
                l += str(num[i+1]) + ' '
            else:
                l += '-1 '
    l += '-1 '
    print(l)