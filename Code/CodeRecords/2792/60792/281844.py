n=int(input())
list1=list(map(int,input().split(" ")))
list2=[]
for i in range(1,len(list1)):
    if list1[i]==1:
        list2.append(list1[i-1])
list2.append(list1[len(list1)-1])
print(len(list2))
for j in range(0,len(list2)-1):
    print(list2[j],end=" ")
print(list2[len(list2)-1])