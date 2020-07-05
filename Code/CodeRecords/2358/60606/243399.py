test_num = int(input())
for i in range(test_num):
    line = input().split(" ")
    n = int(line[0])
    k = int(line[1])
    array = input().split(" ")
    array = [int(x) for x in array]
    array.sort()
    for j in range(len(array)-1,len(array)-k-1,-1):
        print(array[j],end=" ")
    print()