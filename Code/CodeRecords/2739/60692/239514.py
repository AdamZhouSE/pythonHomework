import itertools
list1 = input().split(",")
list2 = []
list3 = []
k = int(list1[0])
n = int(list1[1])
for i in itertools.combinations('123456789', k):
    list2.append(list(i))
for j in list2:
    for k in range(len(j)):
        j[k] = int(j[k])
for m in list2:
    if sum(m) == n:
        list3.append(m)
print(list3)