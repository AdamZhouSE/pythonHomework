def divide(num):
    global ans
    tmp=num//2+num//3+num//4
    if(tmp>num):
        ans+=tmp-num
        divide(num//2)
        divide(num//3)
        divide(num//4)
    return
t=int(input())
for tt in range(t):
    ans=int(input())
    divide(ans)
    print(ans)
