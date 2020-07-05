length=int(input())
array=[[] for _ in range(length)]
for i in range(length):
    temp=input()
    array[i]=list(temp)
list1=[]
list2=[]
for i in range(length):
    for j in range(length):
        if i==j or i==length-j-1:
            list1.append(array[i][j])
        else:
            list2.append(array[i][j])
list1.sort()
list2.sort()
if list1[0]==list1[len(list1)-1] and list2[0]==list2[len(list2)-1] and list1[0]!=list2[0]:
    print("YES")
else:
    print("NO")