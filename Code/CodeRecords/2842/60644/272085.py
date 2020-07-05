def l(x,arr,h):
    ans=h
    max=h

    for i in range(0,len(arr)):
        if arr[i]==x+1:
            ans=ans+1

            if l(i,arr,ans)>max:
                h=l(i,arr,ans)
                max=h
            ans=ans-1


    return h




n=int(input())
arr=[]
for i in range(0,n):
    arr=arr+[int(input())]
res=1
for i in range(0,n):
    if l(i,arr,1)>res:
        res=l(i,arr,1)
print(res)
