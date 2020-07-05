num=int(input())
nums=list(input().split(" "))
res=[]
count=0

for x in nums:
    if x=="1":
        res.append(count)
        count=1
    else:
        count=count+1

res.append(count)
res.remove(0)

print(len(res))

for i in range(0,len(res)):
    if i!=len(res)-1:
        print(str(res[i])+" ",end="")
    else:
        print(res[i])