def dfs(i,s):
    global ans
    if(i==len(arr)-1):
        for j in range(26):
            cnt[j]=0
        for j in range(len(s)):
            if(cnt[ord(s[j])-ord('a')]!=0):
                return
            cnt[ord(s[j])-ord('a')]+=1
        ans=max(ans,len(s))
        return
    i+=1
    dfs(i,s)
    dfs(i,s+arr[i])
ans=0
cnt=[0 for i in range(26)]
arr=eval(input())
dfs(-1,'')
print(ans)