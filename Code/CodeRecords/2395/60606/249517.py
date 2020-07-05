test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    zeroNum = 0
    result = []
    #step 1
    for j in range(1,len(array)):
        if array[j-1] == array[j] and array[j-1] != 0:
            array[j-1] *= 2
            array[j] = 0

    #step 2
    for j in range(len(array)):
        if array[j] == 0:
            zeroNum += 1
        else:
            result.append(array[j])
    for j in range(zeroNum):
        result.append(0)
    result = [str(x) for x in result]
    print(" ".join(result))