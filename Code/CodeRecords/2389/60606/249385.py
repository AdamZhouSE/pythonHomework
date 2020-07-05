test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    for j in range(0,len(array)-1,2):
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
    array = [str(x) for x in array]
    print(" ".join(array))