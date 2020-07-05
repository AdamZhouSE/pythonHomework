list0=input().split()
n=int(list0[0])
m=int(list0[1])
list1=input().split()
list1=[int(list1[i]) for i in range(len(list1))]
for i in range(m):
    list2=input().split()
    list3=[]
    for j in range(int(list2[1])-1,int(list2[2])):
        list3.append(list1[j])
    if list2[0]=='1':
        list3.sort(reverse=True)
    else:
        list3.sort()
    for j in range(int(list2[1])-1,int(list2[2])):
        list1[j]=list3[j-int(list2[1])+1]
print(list1[int(input())-1])