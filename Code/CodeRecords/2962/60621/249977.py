a=[int(x) for x in input().split()]
b=input().split()
def finLocat(nnm,ele:list,p):
    i=(nnm)%p
    gap=0
    while ele[i]!="-1":
        gap+=1
        i=(nnm+gap**2)%p
    return i
def count(s:str):
    if(len(s)>3):
        s=s[len(s)-3:len(s)]
    ans=0
    for i in s:
        ans=ans*32+(ord(i)-ord("A"))
    return ans
ele=["-1" for i in range(a[1])]
st=""
for j in b:
    loc=finLocat(count(j),ele,a[1])
    ele[loc]=j
    st+=(str(loc)+" ")
print(st.rstrip())
