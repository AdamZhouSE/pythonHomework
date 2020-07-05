n=int(input())
list=input().split(",")
res=[]
for i in range(1,len(list)+1):
    for j in range(len(list)-i+1):
        result = 0
        for k in range(j,j+i):
            result+=int(list[k])
        if result>=n:
            res.append(i)
            break
if len(res)==0:
    print(0)
else:
    print(res[0])