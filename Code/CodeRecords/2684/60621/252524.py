a=eval(input())
ans=0
def dp(s:list,i:int,total):
    global ans
    if(ans<total):
        return
    if(i>=len(s)):
        ans=min(total,ans)
        return
    dp(s,i+1,total+s[i])
    dp(s,i+2,total+s[i])

for i in range(a):
    f=int(input())

    te = [int(x) for x in input().split()]
    if f<2:
        print(te[0])
    from functools import reduce
    ans=reduce(lambda x,y:x+y,te)
    dp(te,0,0)
    dp(te,1,0)
    print(ans)

