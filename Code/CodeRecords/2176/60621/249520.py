a=input()
b=[]
for i in range(1,len(a)+1):
    b.append(a[len(a)-i:len(a)])

c=set(b)
b=list(c)
b.sort()
st=""
for i in b:
    st+=str(a.rfind(i)+1)
    if i!=b[len(b)-1]:
        st+=" "
print(st)