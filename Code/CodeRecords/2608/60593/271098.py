def dfs(s,pos):
    global string
    if(s[0] in legal and s[len(s)-1] not in legal):
        ans.append(s)
    if(pos==len(string)-1):
        return
    dfs(s+string[pos+1],pos+1)
    dfs(s,pos+1)
legal=['a','e','i','o','u']
ans=[]
dfs('',0)
ans.sort()
print(ans)