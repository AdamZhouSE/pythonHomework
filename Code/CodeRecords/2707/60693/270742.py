p=[1]*100
def find(x):
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

def swap_couples(arr):
    n=len(arr)
    # initialize p, all couples are a joint set
    for i in range(0,n,2):
        p[i+1]=i
        p[i]=i

    for i in range(0,n,2):
        p[find(arr[i+1])]=find(arr[i])

    res=n//2  # couple number
    for i in range(n):
        if p[i]==i:res-=1
    return res

arr=eval(input())
print(swap_couples(arr))