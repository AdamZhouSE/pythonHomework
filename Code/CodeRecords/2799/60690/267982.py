num=int(input())
list=input().split(" ")
for i in range(num):
    list[i]=int(list[i])

res=""
for i in range(num):
    while list[i]%2==0:
        list[i]/=2
    while list[i]%3==0:
        list[i]/=3

list2=[]
for i in range(num):
    if list[i] not in list2:
        list2.append(list[i])
if len(list2)==1:
    print("Yes")
else:
    print("No")