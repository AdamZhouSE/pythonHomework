words=[]
try:
    while True:
        words.append(input())
except EOFError:
    pass
def isValid(pre,next):
    count=0
    i=0
    j=0
    while i<len(pre):
        if pre[i]!=next[j]:
            j+=1
            count+=1
        else:
            i+=1
            j+=1
        if count>1:
            return False
    return True
ans=[]
def dfs(words,pre,temp,used,ans):
    if len(temp)>len(ans):
        ans.clear()
        for p in temp:
            ans.append(p)
    for i in range(0,len(words)):
        if i not in used:
            if pre=="":
                used.append(i)
                temp.append(i)
                dfs(words, words[i], temp, used, ans)
                used.pop()
                temp.pop()
            elif len(words[i])==len(pre)+1:
                if isValid(sorted(pre),sorted(words[i])):
                    used.append(i)
                    temp.append(i)
                    dfs(words,words[i],temp,used,ans)
                    used.pop()
                    temp.pop()

dfs(words,"",[],[],ans)
print(len(ans))
for i in ans:
    print(words[i])