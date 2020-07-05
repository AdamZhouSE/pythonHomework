list=input()[1:-1]
list=list.split(",")
for i in range(len(list)):
    list[i]=int(list[i])
anslist=[]
for i in range(len(list)-1):
    count=0
    for j in range(i+1,len(list)):
        if(list[j]<list [i]):
            count+=1
    anslist.append(count)
anslist.append(0)
print(anslist)