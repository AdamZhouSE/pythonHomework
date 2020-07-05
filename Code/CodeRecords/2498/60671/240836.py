str=input()
list=str[1:-1]
llist=list.split(",")
list=[]
for x in llist:
    list.append(int(x))
temp1=[]
temp2=[]
for i in list:
    if(i%2==0):
        temp2.append(i)
    else:
        temp1.append(i)
length=len(list)
half=length//2
fin=[]
for i in range(half):
    fin.append(temp2[i])
    fin.append(temp1[i])
if((length%2)!=0):
    fin.append(temp2[-1])
print(fin)