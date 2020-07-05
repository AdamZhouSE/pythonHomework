test_num = int(input())
for i in range(test_num):
    line = input().split(" ")
    n = int(line[0])
    sum = int(line[1])
    array = input().split(" ")
    array = [int(x) for x in array]
    sentinel = 0
    result = []
    for j in range(len(array)):
        temp = 0
        result = []
        for k in range(j,len(array)):
            if k > j and array[k-1] <= array[k]:
                temp += array[k]
                result.append(k+1)
            elif k == j :
                temp += array[k]
                result.append(k+1)
            else:
                break
            if temp == sum:
                sentinel = 1
                break
            elif temp > sum:
                break
        if sentinel == 1:
            break
    if sentinel == 1:
        print(result[0],end=" ")
        print(result[-1])

    else:
        print(-1)