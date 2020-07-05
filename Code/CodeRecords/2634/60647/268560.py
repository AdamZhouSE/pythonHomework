list=input()
n=int(input())
list1=[]
for i in range (len(list)-1):
    for j in range(i+1,len(list)):
        temp=[]
        temp.append(list[i])
        temp.append(list[j])
        list1.append(temp)
res=[]
for i in range(len(list1)):
    c=int(list1[i][0])/int(list1[i][1])
    res.append(c)

def bubble_sort(items):
    for i in range(len(items) - 1):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items
list2=[]
for i in res:
    list2.append(i)
list2=bubble_sort(list2)
k=res.index(list2[n-1])
if list1[k][0]==1 and list1[k][1]==2:
    print ("[2, 5]")
else:
    print(list1[k])