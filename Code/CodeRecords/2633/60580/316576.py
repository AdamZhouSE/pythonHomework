number = input().split()
array = input().split()
for i in range(int(number[0])):
    array[i] = int(array[i])
for i in range(int(number[1])):
    temp = input().split()
    if temp[0] == '1':
        L = int(temp[1])
        R = int(temp[2])
        K = int(temp[3])
        D = int(temp[4])
        for i in range(L, R + 1):
            array[i] = array[i] + K + (i - L + 1) * D
    else:
        print(array[int(temp[1]) - 1])
