def sumall(list):
    sum = 0
    for i in list:
        sum += i
    return sum

test_num = int(input())
for i in range(test_num):
    line1 = input().split(" ")
    n = int(line1[0])
    m = int(line1[1])
    x = int(line1[2])
    array1 = input().split(" ")
    array2 = input().split(" ")
    array1 = [int(x) for x in array1]
    array2 = [int(x) for x in array2]
    array1.sort()
    array2.sort()
    for j in range(n):
        for k in range(m):
            if array1[j] + array2[k] == x:
                print(array1[j],end=" ")
                print(array2[k])


