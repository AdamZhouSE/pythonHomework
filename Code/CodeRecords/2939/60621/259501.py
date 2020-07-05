a=[int(x) for x in input().split()]
counting=[1]
ans=[]
while len(ans)<a[0]:
    p=counting.pop(0)
    counting.append(2*p+1)
    counting.append(4*p+5)
    ans.append(p)
    counting.sort()
st=""
for i in ans:
    st+=str(i)

de=[int(x) for x in st]
m=a[1]
index=0
while index<len(de)-1 and m>0:
    if de[index]<de[index+1]:
        de.pop(index)
        m-=1
        index=0
    else:
        index+=1
ans=""
for i in de:
    ans+=str(i)
print(st,end="\n")
print(ans,end="")