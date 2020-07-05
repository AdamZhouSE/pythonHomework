def dfs(s,pos):
    global string
    if(len(s)):
        if(s[0] in legal and s[len(s)-1] not in legal and s not in ans):
            ans.append(s)
    if(pos==len(string)-1):
        return
    dfs(s+string[pos+1],pos+1)
    dfs(s,pos+1)
legal=['a','e','i','o','u']

n=int(input())
for i in range(n):
    ans=[]
    string=input()
    dfs('',-1)
    ans.sort()
    print(-1 if not len(ans) else ' '.join(ans))