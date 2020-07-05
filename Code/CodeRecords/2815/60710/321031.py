num=int(input())
temp = list(input().split(" "))
lists = []

for x in temp:
    lists.append(int(x))

res=0
result=[]
ZeroNum=0
for a in lists:
    if a>=1:
        result.append(1)
        res=res+a-1
    if a<=-1:
        res=res-1-a
        result.append(-1)
    if a==0:
        res=res+1
        ZeroNum=ZeroNum+1

if ZeroNum==0 and result.count(-1)%2==1:
    res=res+2
print(res)
