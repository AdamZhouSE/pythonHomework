n=int(input())
list1=[int(i) for i in input().split()]
list2=[]
for i in list1:
    if (not i in list2) and (not i==0):
        list2.append(i)
print(len(list2))