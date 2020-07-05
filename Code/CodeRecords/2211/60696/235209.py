arr = [int(i) for i in input().split()]
n = arr[0]
k = arr[1]
names = []
for i in range(n):
    arr = input().split()
    if int(arr[1])==0:
        names.append(arr[0])
    else:
        parent = int(arr[1])
        names.append(arr[0] + names[parent-1])
for i in range(k):
    name_str = input()
    count = 0
    for j in range(len(names)):
        if names[j].__contains__(name_str) and names[j].index(name_str)==0:
            count += 1
    print(count)