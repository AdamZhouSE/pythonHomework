strs=input()
res=[]
for i in range(len(strs)):
    s=strs[i:]+strs[0:i]
    res.append(s)
res.sort()
s=""
for i in range(len(res)):
    s=s+res[i][len(res[i])-1]
print(s,end="")
    