pNum,height=map(int,input().split())
data=input().split()
num=0
for i in range(pNum):
    if int(data[i])>height:
        num+=1
res=num+pNum
print(res)