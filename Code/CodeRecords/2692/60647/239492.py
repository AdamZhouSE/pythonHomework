list=input()
x=int(input())
all=0
for i in range(len(list)):
    all=all+list[i]
all=int(all/x)
res=max(all,max(list))
temp=True
while temp==True:
    list1=[]
    for num in list:
        list1.append(num)
    day=0
    for i in range(len(list1)):
        tempres=0
        if list1[i]!=0:
            day=day+1
            for j in range(i,len(list1)):
                if tempres+list1[j]>res:
                    break
                else:
                    tempres=tempres+list1[j]
                    list1[j]=0
    if day<=x:
        temp=False
    else:
        res=res+1
print(res)