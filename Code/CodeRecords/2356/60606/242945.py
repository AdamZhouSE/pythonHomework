def isMax(index,list):
    for i in range(index):
        if list[i] > list[index]:
            return False
    return True
test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array1 = [int(x) for x in array]
    array2 = [int(x) for x in array]
    array2.sort()
    sentinel = 0
    for j in range(1,len(array1)-1):
        if array1[j] == array2[j] and isMax(j,array1):
            sentinel = 1        
            print(array1[j])
            break
    if sentinel == 0:
        print(-1)

