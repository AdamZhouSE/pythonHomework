n=int(input())

a=input().split(" ")
a=[int(x) for x in a]

#下面删除数组中有倍数关系的：
i=0
while i<len(a)-1:
    j=i+1
    if a[j]%a[i]==0:
        del a[j]
    elif a[i]%a[j]==0:
        del a[i]
        i=i-1
    i=i+1


n=len(a)    
m=min(a)

if n==1:
    print(a[0])
else:
    esult=0
    for i in range(1,m+1):
        j=0
        while j<n:
            if a[j]%i!=0:
                break
            j=j+1
       
        if j==n:
            result=result+1
    print(result)
