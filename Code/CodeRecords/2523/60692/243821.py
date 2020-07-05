list1 = input()[2:-2].split("],[")
list1 = [[int(i) for i in e.split(",")] for e in list1]
for i in range(1,min(len(list1), len(list1[0]))):
    for j in range(len(list1) - i):
        for k in range(len(list1[0]) - i):
            if list1[j][k] > list1[j + 1][k + 1]:
                list1[j][k], list1[j + 1][k + 1] = list1[j + 1][k + 1], list1[j][k]
print(list1)