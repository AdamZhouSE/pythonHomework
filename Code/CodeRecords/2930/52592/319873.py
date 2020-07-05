a=int(input())

b=input().split()
l=[]
for i in range(len(b)):
    l.append(int(b[i]))

index=0
for j in range(1,a-1):
    
    if (l[j]<l[j-1])&(l[j]<l[j+1]):
        index+=1
    if (l[j]>l[j-1])&(l[j]>l[j+1]):
        index+=1
print(index)