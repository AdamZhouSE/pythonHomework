def find_pair(arr1, arr2, num):
    res = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if int(arr1[i]) + int(arr2[j]) == num:
                res.append((arr1[i], arr2[j]))
                break
    return res


result = []
for i in range(int(input())):
    number = int(input().split()[2])
    array1 = input().split()
    array2 = input().split()
    result.append(find_pair(array1, array2, number))
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j][0], result[i][j][1])