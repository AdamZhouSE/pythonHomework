a=eval(input())
tar=int(input())
l=0
r=len(a)-1
find=-1
while(l<=r):
    mid=(l+r)//2
    if(a[mid]==tar):
        find=mid
        break
    if(a[mid]<tar):
        l=mid+1
    else:
        r=mid-1
print(find)