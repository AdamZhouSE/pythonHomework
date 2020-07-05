test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    mul = 0
    for j in range(len(array)-2):
        for k in range(j+1,len(array)-1):
            for m in range(k+1,len(array)):
                if array[j] * array[k] *array[m] > mul:
                    mul = array[j] * array[k] *array[m]
    print(mul)
