def p(n):
    res=[]
    for i in range(n):
        re=[]
        for j in range(n):
            re.append(0)
        res.append(re)
    return res
def find(arr,s,t):
    k=s
    count=0
    while not k==t:
        for i in range(len(arr)):
            if arr[k-1][i]>0:
                count=count+arr[k-1][i]
                k=i+1
    return count
n,m,s,t=[int(x) for x in input().split(" ")]
arr=p(n)
for p in range(m):
    a,b,c=[int(x) for x in input().split(" ")]
    arr[a-1][b-1]=c
count=find(arr,s,t)
print(count)
    