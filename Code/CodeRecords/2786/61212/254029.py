num=int(input())
lists=list(input().split(" "))
res=[]

for i in range(0,num):
    res.append(int(lists[i]))

k=1
while True:
    temp=[]
    for x in res:
        if x>=k:
            temp.append(x)

    if len(temp)==0:
        break
    res.remove(min(temp))
    k=k+1

print(k-1)
