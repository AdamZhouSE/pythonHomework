string=input()
strs=input()[1:-1].split(",")
for i in range(0,len(strs)):
    strs[i]=strs[i][1:-1]
res=[]
for i in range(0,len(strs)):
    j=0
    k=0
    while j<len(strs[i]) and k<len(string):
        if strs[i][j]==string[k]:
            j=j+1
            k=k+1
        else:
            k=k+1
    if j==len(strs[i]):
        res.append(strs[i])
res.sort(key=lambda x:len(x))
result=[]
n=len(res[-1])
for i in range(0,len(res)):
    if len(res[i])==n:
        result.append(res[i])
result.sort()
print(result[0])