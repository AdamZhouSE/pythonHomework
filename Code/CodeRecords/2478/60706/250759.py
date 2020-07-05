t=int(input())
for i in range(t):
    list=input().split(' ')
    a=int(list[0])
    b=int(list[1])
    sub=b-a
    n=int(input())
    ans=a+sub*(n-1)
    print(ans)
    