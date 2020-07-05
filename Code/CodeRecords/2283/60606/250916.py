test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    array.sort()
    array = [str(x) for x in array]
    print(" ".join(array))