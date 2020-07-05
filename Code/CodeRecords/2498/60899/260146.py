a = "".join(input().split("["))
a = "".join(a.split("]"))
a = list(map(int,a.split(",")))
listOfodd = []
listOfeven = []
for i in range(len(a)):
    if a[i]%2 == 1:
        listOfodd.append(a[i])
    else:listOfeven.append(a[i])
listOfodd.sort()
listOfeven.sort()
list1 = []
for i in range(len(a)//2):
    list1.append(listOfeven[i])
    list1.append(listOfodd[i])
print(list1)

