# 7
n = int(input())
for i in range(n):
    input()
    num = input().split()
    for i in range(len(num)):
        num[i] = int(num[i])
    l = []
    for i in range(len(num)):
        if i == len(num) -1:
            l.append(num[i])
            break
        if num[i] > sum(num[i+1:]):
            l.append(num[i])
    print(l)