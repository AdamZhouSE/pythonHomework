a= int(input())
o = [int(i) for i in input().split(' ')]
t = [int(i)-1 for i in input().split(' ')]
for i in range(a):
    res = 0
    l = [True for j in range(a)]
    while l[i]:
        res += o[i]
        l[i] = False
        i = t[i]
    print(res)