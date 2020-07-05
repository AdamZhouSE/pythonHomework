stairs=int(input())
list=input().split(" ")
list2=[]

sNum=0
for i in list:
    if i=="1": sNum+=1

for i in range(1,len(list)):
    if list[i]=="1":
        list2.append(list[i-1])
list2.append(list[-1])
print(sNum)
for i in range(len(list2)-1):
    print(list2[i],end=" ")
print(list2[-1])
