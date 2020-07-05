a=[int(x) for x in input().split()]
m,n=a[0],a[1]
b=[[i+1,int(j)] for i,j in enumerate(input().split())]
st=""
def findkey(ele):
    return ele[1]
for i in range(n):
    c=[int(x) for x in input().split()]
    temp=[x for x in b[c[0]-1:c[1]]]
    temp.sort(key=findkey)
    st=st+str(temp[0][1])+" "
print(st.rstrip(),end=" ")