test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    array.sort()
    sentinel = 0
    num = 1
    for j in range(len(array)):
        if j< len(array) - 1 and array[j] != array[j+1]:
            if num % 2 == 1:
                sentinel = 1
                print(array[j])
                break
            else:
                num = 1
        elif j == len(array) - 1:
            if array[j-1] == array[j]:
                if num % 2 == 1:
                    sentinel = 1
                    print(array[j])
                    break
            else:
                sentinel = 1
                print(array[j])
        else:
            num += 1
    if sentinel == 0:
        print(0)
