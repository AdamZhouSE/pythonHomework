num_test = int(input())
info_list = []
mat1_list = []
mat2_list = []
for i in range(num_test):
    info = input().split()
    info = [int(x) for x in info]
    num_line = info[0]
    mat1 = []
    mat2 = []
    for j in range(num_line):
        array = input().split()
        array = [int(x) for x in array]
        for ch in array:
            mat1.append(ch)
    for j in range(num_line):
        array = input().split()
        array = [int(x) for x in array]
        for ch in array:
            mat2.append(ch)
    info_list.append(info)
    mat1_list.append(mat1)
    mat2_list.append(mat2)
for i in range(num_test):
    info = info_list[i]
    mat1 = mat1_list[i]
    mat2 = mat2_list[i]
    goal = info[1]
    count = 0
    for j in range(len(mat1)):
        if mat1[i] + mat2[i] == goal:
            count = count + 1
    print(count)