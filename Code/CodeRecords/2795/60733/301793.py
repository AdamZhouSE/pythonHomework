n=int(input())
a=input().split()
for i in range(n):
    a[i]=int(a[i])
a.sort()
b=list(set(a))
b.sort()
if(len(b)==3 and 2*b[1]==(b[0]+b[2])):
    print(b[2]-b[1])
elif(len(b)==1):
    print(0)
elif(len(b)==2):
    if (b[0]+b[1])%2==0 : print(b[1]-(b[0]+b[1])//2)
    else : print(b[1]-b[0])
else:
    print(-1)