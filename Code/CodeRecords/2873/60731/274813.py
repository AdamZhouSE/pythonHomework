n,m=map(int,input().split())
numStr=input().split()
buttonStr=input().split()
res=[]
for i in range(n):
    if numStr[i] in buttonStr:
        res.append(numStr[i])
for j in range(len(res)-1):
    print(res[j],end=' ')
print(res[len(res)-1])
