t=int(input())
list0=[]
def find(i,j):
    if j-i<=1:
        return 0
    else:
        sum=0
        if i==0:
            maxn=fmax(0,j)
            maxi=findin(maxn,0,j-1)
        else:
            maxn=fmax(i+1,n)
            maxi=findin(maxn,+1,n)
        if list0[i]<list0[j]:
            for m in range(maxi+1,j):
                sum+=maxn-list0[m]
            if sum==0: return 0
            return sum+find(0,maxi)
        else:
            for m in range(i+1,maxi):
                sum+=maxn-list0[m]
            if sum==0:
                return 8
            return sum+find(maxi,n-1)
def fmax(a,b):
    maxn=list0[a]
    for i in range(a,b):
        if list0[i]>maxn:
            maxn=list0[i]
    return maxn
def findin(num,a,b):
    for i in range(a,b+1):
        if list0[i]==num:
            return i

for k in range(t):
    n=int(input())
    list0=input().split()
    list0=[int(x) for x in list0]
    max0=max(list0)
    i=list0.index(max0)
    if i==0: print(find(i,n-1))
    elif i==n-1: print(find(0,i))
    else: print(find(0,i)+find(i,n-1))
