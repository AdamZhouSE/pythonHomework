a=eval(input())
ans=0
def dp(s:str,i:int,length,maxim):
    global ans
    if(i==len(s)):
        ans=max(length,ans)
        return
    if(ord(s[i])>maxim):
        dp(s,i+1,length+1,ord(s[i]))
        dp(s,i+1,length,maxim)
    else:
        dp(s, i + 1, length, maxim)
for i in range(a):
    b=input()
    ans=0
    dp(b,0,0,ord("a")-1)
    print(ans)



