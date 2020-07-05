from operator import itemgetter
list1 = eval(input())
k = int(input())
lenl=int(len(list1)*(len(list1)-1)/2)
list2=[[0 for i in range(3)]for i in range(lenl)]
count=0
for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        list2[count]=[list1[i]/list1[j],list1[i],list1[j]]
        count+=1
list2.sort()
m = list2[k - 1]
list3 = []
list3.append(list2[k-1][1])
list3.append(list2[k-1][2])
print(list3)
