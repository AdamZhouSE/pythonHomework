def search(a,b):
    mid=find(a,b)
    if mid==-1:
        return [-1,-1]
    first=find(a[:mid+1],b)
    last=find(a[mid:],b)+mid
    c=[]
    c.append(first)
    c.append(last)
    return c
def find(a,b):
    l=0
    r=len(a)
    while r-l>0:
        mid=(l+r)//2
        if a[mid]>b:
            r=mid-1
        elif a[mid]<b:
            l=mid+1
        else:
            break
    if r==l and a[r]!=b:
        return -1
    return mid
a=input().split(',')
a=[int(x) for x in a]
b=int(input())
print(search(a,b))