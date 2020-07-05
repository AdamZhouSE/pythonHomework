n=int(input())
a=[]
for i in range(n):
    info=input().split(',')
    a0=[int(y) for y in info]
    a.append(a0)
print(a)