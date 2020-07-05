n=int(input())
k=int(input())
list=[]
for i in range(1,n+1): list.append(i)
res=""
while 1:
    if k==1:
        res=res+str(list[0])+str(list[1])
        break
    elif k==2:
        res+=str(list[1])+str(list[0])
        break
    else:
        oneNum = 1
        for i in range(1,n): oneNum*=i
        res+=str(list[int(k/oneNum)])
        list.pop(int(k/oneNum))
        k=k%oneNum
        n-=1
print(res)