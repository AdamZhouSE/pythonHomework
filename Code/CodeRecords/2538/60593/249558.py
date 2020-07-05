a=eval(input())
l=0
r=len(a)
while(l<r):
    if(a[l]==l+1):
        l+=1
    elif(a[l]<l+1 or a[l]>r or a[a[l]-1]==a[l]):
        r-=1
        a[l]=a[r]
    else:
        tmp=a[l]
        a[l]=a[a[l]-1]
        a[tmp-1]=tmp
print(l+1)