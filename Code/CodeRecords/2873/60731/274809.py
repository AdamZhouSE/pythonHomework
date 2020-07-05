n,m=map(int,input().split())
numStr=input().split()
buttonStr=input().split()
res=[]
for i in range(n):
    if numStr[i] in buttonStr:
        res.append(numStr[i])
for j in range(len(res)):
    print(res[j],end=' ')