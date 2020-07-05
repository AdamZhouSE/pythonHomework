test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    zeroNum = 0
    result = []
    for j in range(len(array)):
        if array[j] == 0:
            zeroNum += 1
        else:
            result.append(array[j])
    for j in range(zeroNum):
        result.append(0)
    result = [str(x) for x in result]
    for j in result:
        print(j,end=" ")
    print()

