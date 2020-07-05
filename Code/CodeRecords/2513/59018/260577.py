n=int(input())
a=[]
for i in range(n):
    info=input().split(',')
    for y in info:
        a.append(int(y))
k=int(input())
a.sort()
print(a[k-1])

         
