# 11
n = int(input())
l = []
for i in range(n):
    inp = input()
    num = inp.split(',')
    for i in range(len(num)):
        num[i] = int(num[i])
    l = l + num
k = int(input())

l.sort()
print(l[k-1])