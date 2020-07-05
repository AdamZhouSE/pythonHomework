n=int(input())
l=input().split(" ")
for i in range(n): l[i]=int(l[i])
l.sort()
l1,l2=0,0
for i in range(int(n/2)):
    l1+=l[i]
for i in range(int(n/2),n):
    l2+=l[i]
res=l1**2+l2**2
print(res)