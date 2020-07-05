test_num = int(input())
for i in range(test_num):
    result = []
    line1 = input().split(" ")
    size1 = int(line1[0])
    size2 = int(line1[1])
    array1 = input().split(" ")
    array2 = input().split(" ")
    array1 = [int(x) for x in array1]
    array2 = [int(x) for x in array2]
    array2.sort()
    label1 = 0
    label2 = 0
    while True:
        if array1[label1] <= array2[label2]:
            result.append(array1[label1])
            label1 += 1
        else:
            result.append(array2[label2])
            label2 += 1
        if label1 == size1:
            result += array2[label2:]
            break
        elif label2 == size2:
            result += array1[label1:]
            break
    for j in result:
        print(j,end=" ")
    print()
