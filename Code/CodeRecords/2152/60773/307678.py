num=int(input())
l1=input().split(" ")
l2=input().split(" ")
for i in range(num):
    l1[i]=int(l1[i])
    l2[i]=int(l2[i])
dic={}
for i in range(num):
    index=l2[i]
    sum=l1[i]
    route=[]
    route.append(i+1)
    while(True):
        if index in route:
            break
        sum=sum+l1[index-1]
        route.append(index)
        index=l2[index-1]
        if index in route:
            break
    print(sum)