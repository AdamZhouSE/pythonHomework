str1=input()
list1=str1.split(",")
listnum=[]
for x in list1:
    listnum.append(int(x))
length=len(listnum)
new=[1]*length
count=1
for i in range(1,length):
    for j in range(i):
        if(listnum[j]<listnum[i]):
            new[i]=max(new[i],1+new[j])
    count=max(count,new[i])

print(count)


