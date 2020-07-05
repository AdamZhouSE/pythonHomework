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
print(st)
de=[int(x) for x in st]
de.sort()
de=de[a[1]:]
st2=""
for i in de[::-1]:
    st2+=str(i)
print(st2)