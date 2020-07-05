list1=eval(input())
k=int(input())
list2=[]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        list2.append(abs(list1[j]-list1[i]))
list2.sort()
print(list2[k-1])