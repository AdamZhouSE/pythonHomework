a=[int(x) for x in input().split()]
m,n=a[0],a[1]
b=[[i+1,int(j)] for i,j in enumerate(input().split())]
st=""
def findkey(ele):
    return ele[1]
t=[]
for i in range(n):
    c=[int(x) for x in input().split()]
    t.append(c)
print(t)