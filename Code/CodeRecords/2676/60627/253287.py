# 14
n = int(input())
for i in range(n):
    _,k = input().split()
    k = int(k)
    num = input().split()
    for i in range(len(num)):
        num[i] = int(num[i])
    l = []
    for i in range(len(num)):
        if i + k >len(num):
            break
        l.append(sum(num[i:i+k]))
    print(max(l))
    