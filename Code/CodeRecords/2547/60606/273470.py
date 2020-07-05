import math
test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    array.sort()
    k = int(input())
    set1 = set()
    for j in range(len(array)):
        for m in range(j+1,len(array)):
            if math.fabs(array[j] - array[m]) == k:
                x = str(array[j])
                y = str(array[m])
                set1.add(x+y)
    print(len(set1))