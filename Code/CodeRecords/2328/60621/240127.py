a=[int(x) for x in input().split(",")]
def find(ele,n):
    te=[x for x in ele]
    te.sort()
    maximum=-1
    for i in te:
        if(i>n):
            break
        else:
            maximum=max(maximum,i)
    return maximum
if 2 in a:
    if 4 in a and a.count(0)>=2:
        m=[2,4,0,0]
    m = [2, 3, 5, 9]
else:
    m=[1,9,5,9]

st=""
for n in m:
    x=find(a,n)
    if(x==-1):
        str=""
        break
    else:
        a.remove(x)
        st+=str(x)
if(len(st)!=0):
    st=st[0:2]+":"+st[2:4]
print(st)
