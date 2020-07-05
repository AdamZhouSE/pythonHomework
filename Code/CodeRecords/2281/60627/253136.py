# 8
n = int(input())
for i in range(n):
    input()
    num = input().split()
    for i in range(len(num)):
        num[i] = int(num[i])
    l = ''
    for i in range(len(num)):
        if i == len(num) -1:
            l += str(num[i])
            break
        if num[i] >= max(num[i+1:]):
            l += str(num[i]) + ' '
    
    print(l)