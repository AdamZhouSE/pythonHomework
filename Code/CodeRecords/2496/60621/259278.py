a=input()
b={}
c=[]
for i in a:
    if i in b:
        index=b[i]
        c[index][1]+=1
    else:
        b[i]=len(c)
        c.append([i,1])

def sec(ele):
    return ele[1]
c.sort(key=sec)
st=""
i,j=0,1
while i<len(c) and j <len(c):
    st += c[i][0]
    st += c[j][0]
    c[i][1] -= 1
    c[j][1] -= 1
    if c[i][1]==0:
        i+=1
        if i==j:
            i+=1
    if c[j][1]==0:
        j+=1
        if j==i:
            j+=1

t=min(i,j)
l=len(st)
if t<len(c):
    k=0
    while k<len(st) and c[t][1]>0:
        if st[k]!=c[t][0] and (k<1 or st[k-1]!=c[t][0]):
            st=st[0:k]+c[t][0]+st[k:]
            c[t][1]-=1
        else:
            k+=1
if c[t][1]>0:
    print("")
else:
    print(st)


