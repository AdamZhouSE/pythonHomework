n=int(input())
list=[]
for i in range(n):
    list1=input().split(",")
    list.append(list1)
k=int(input())
list2=[]
for i in range(len(list)):
    for j in range(len(list[0])):
        list2.append(int(list[i][j]))
list2.sort()
print(list2[k-1])