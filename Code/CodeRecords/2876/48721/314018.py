a=int(input())
b=input().split()
l=[]
index=0
for i in range(len(b)):
    l.append(int(b[i]))
for j in range(1,len(l)-1):
    if l[j]==0:
        if l[j-1]==1 & l[j+1]==1:
            l[j+1]=0
            index+=1
print(index)