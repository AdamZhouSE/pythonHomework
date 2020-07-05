num_test = int(input())
info_list = []
array1_list = []
array2_list = []
array3_list = []
for i in range(num_test):
    info = int(input())
    info_list.append(info)
    array1 = input().split()
    array2 = input().split()
    array3 = input().split()
    array1 = [int(x) for x in array1]
    array2 = [int(x) for x in array2]
    array3 = [int(x) for x in array3]
    array1_list.append(array1)
    array2_list.append(array2)
    array3_list.append(array3)
for i in range(num_test):
    count = 0
    array1 = array1_list[i]
    array2 = array2_list[i]
    array3 = array3_list[i]
    for j in range(len(array1)):
        for k in range(len(array3)):
            if array1[j] == array2[j] + array3[k]:
                count = count + 1
    print(count)