string=input()[1:-1]
list=string.split(",")
number=int(input())
for i in range(len(list)):
    list[i]=int(list[i])
anslist=[]
for i in range(len(list)-1):
    for j in range(len(list)-1,i,-1):
        anslist.append([list[i],list[j]])


print(anslist[-number])