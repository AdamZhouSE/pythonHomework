list=input().split(",")
list[0]=list[0][1:2]
list[-1]=list[-1][0:1]
max=int(list[0])
res=0
for i in range(1,len(list)):
    if max<int(list[i]):
        max=int(list[i])
        res=res+1
print(res+1)