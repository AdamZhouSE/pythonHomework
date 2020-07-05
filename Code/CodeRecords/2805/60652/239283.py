n=int(input())
l=list(map(int,input().split()))
L=[]
length=1
if len(l)==1:
    L.append(length)
for i in range(0,len(l)-1):
    if l[i]<l[i+1]:
        length+=1
        if i==len(l)-2:
            L.append(length)
    else:
        L.append(length)
        length=1
print(max(L))