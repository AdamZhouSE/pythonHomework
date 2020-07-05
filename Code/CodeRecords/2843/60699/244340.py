input()
list1=list(map(int,input().split(' ')))
list2=[]
list2.append(list1[len(list1)-1])
for i in range(len(list1)-1,0,-1):
    list2.append(list1[i]+list1[i-1])
list2.reverse()
for i in range(0,len(list2)):
    if i != len(list2)-1:
        print(list2[i],end=" ")
    else:
        print(list2[i])