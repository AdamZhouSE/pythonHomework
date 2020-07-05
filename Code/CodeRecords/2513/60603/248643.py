num=int(input())
list=[]
for i in range(0,num):
    str=input()
    str=str.split(",")
    for j in str:
        list.append(j)
for i in range(0,len(list)):
    list[i]=int(list[i])
list.sort()
k=int(input())
print(list[k-1])
