n=int(input())
ans=0
min=101
for i in range(0,n):
    list=input().split(' ')
    a=int(list[0])
    p=int(list[1])
    if p<min:
        ans=ans+a*p
        min=p
    else:
        ans=ans+a*min
print(ans)
    