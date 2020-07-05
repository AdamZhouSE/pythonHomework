from itertools import combinations

k,n=map(int,input().split(","))
list1=[1,2,3,4,5,6,7,8,9]
list2=[]
for i in range(0,len(list1)):
    list2+=list(combinations(list1,i))
list2=[x for x in list2 if len(x)==k]
list3=[]
for j in list2:
    if sum(j)==n:
        list3.append(list(j))
print(list3)