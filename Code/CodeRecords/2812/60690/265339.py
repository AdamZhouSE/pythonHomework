num=int(input())
list=input().split(" ")

for i in range(num):
    list[i]=int(list[i])

list.sort(reverse=True)
list2=[]
for i in list:
    if i not in list2 and i!=0:
        list2.append(i)

print(len(list2))
