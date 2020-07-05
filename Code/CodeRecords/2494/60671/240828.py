str=input()
list=str[1:-1]
llist=list.split(",")
list=[]
for x in llist:
    list.append(int(x))
count=0
length=len(list)
for i in range(length):
    for j in range(i+1,length):
        if(list[i]>(2*list[j])):
            count+=1
print(count)