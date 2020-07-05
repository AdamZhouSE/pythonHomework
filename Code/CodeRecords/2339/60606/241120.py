test_num = int(input())
for i in range(test_num):
    sum = 0
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    for j in range(len(array)):
        for k in range(j+1,len(array)):
            if array[j] > array[k]:
                sum += 1
    print(sum)