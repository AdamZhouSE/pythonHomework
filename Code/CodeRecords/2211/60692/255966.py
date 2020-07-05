n_k = input().split(" ")
n = int(n_k[0])
k = int(n_k[1])
list1 = []
names = []
count = []
for i in range(n):
    list2 = input().split(" ")
    if int(list2[1]) == 0:
        list1.append(list2[0])
    else:
        list1.append(list2[0]+list1[int(list2[1]) - 1])
for j in range(k):
    names.append(input())
for p in names:
    counter = 0
    for q in list1:
        if q[0:len(p)] == p:
            counter += 1
    count.append(counter)
print(list1)
for r in count:
    print(r)