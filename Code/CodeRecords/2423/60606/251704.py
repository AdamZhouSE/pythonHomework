test_num = int(input())
for i in range(test_num):
    line = input().split(" ")
    n1 = int(line[0])
    n2 = int(line[1])
    array1 = input().split(" ")
    array1 = [int(x) for x in array1]
    array2 = input().split(" ")
    array2 = [int(x) for x in array2]
    set1 = set()
    set2 = set()
    for j in array1:
        set1.add(j)
    for j in array2:
        set2.add(j)
    if set2.issubset(set1):
        print("Yes")
    else:
        print("No")