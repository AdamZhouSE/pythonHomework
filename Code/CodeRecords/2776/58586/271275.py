words=eval(input())
ans=[]
def dfs(words,temp,depth):
    if len(temp)==0:
        if depth>=2:
            return True
        else:
            return False
    for i in range(0,len(words)):
        if len(words[i])>len(temp):
            continue
        else:
            if temp.find(words[i])!=-1:
                t=temp
                temp=temp.replace(words[i],"")
                if dfs(words,temp,depth+1):
                    return True
                temp=t
    return False
# dfs(words,"",0)
for i in range(len(words)):
    if dfs(words,words[i],0):
        ans.append(words[i])
print(ans)