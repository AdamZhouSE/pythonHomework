s=input()
res=[]
depth=0
for i in range(len(s)):
    if s[i]==')':
        depth-=1
    res.append(depth)
    if s[i]=='(':
        depth+=1
print(res)