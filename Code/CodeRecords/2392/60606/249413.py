test_num = int(input())
for i in range(test_num):
    line1 = input().split(" ")
    n = int(line1[0])
    x = int(line1[1])
    array = input().split(" ")
    array = [int(x) for x in array]
    sentinel = 0
    for j in range(len(array)):
        for k in range(j+1,len(array)):
            if array[j] * array[k] == x:
                sentinel = 1
    if sentinel == 1:
        print("Yes")
    else:
        print("No")