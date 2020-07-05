num = int(input())
list1 = []
for i in range(num*2):
    list1.append(input())
for j in range(0, len(list1) - 1, 2):
    list2 = []
    n = int(list1[j])
    list3 = list1[j + 1].split(" ")
    m = 1
    for k in range(len(list3)):
        m *= int(list3[k])
    for p in range(len(list3)):
        list2.append(str(m//int(list3[p])))
    print(" ".join(list2)+" ")