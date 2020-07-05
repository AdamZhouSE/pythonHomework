list=input()
k=int(input())
x=int(input())
for i in range (len(list)):
    if(list[i]>=x):
        list[i]=list[i]-x
    else:
        list[i]=x-0.1-list[i]
for i in range(len(list)):
    for j in range(0,len(list)-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
res=[]
for i in range(0,k):
    res.append(list[i])
for i in range(0,k):
    if isinstance(res[i],int)==False:
        res[i]=res[i]+0.1
        res[i]=int(x-res[i])
    else:
        res[i]=res[i]+x
for i in range(len(res)):
    for j in range(0,len(res)-i-1):
        if res[j]>res[j+1]:
            res[j],res[j+1]=res[j+1],res[j]
print(res)