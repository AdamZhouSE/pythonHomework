import math
test_num = int(input())
for i in range(0, test_num):
    size = int(input())
    str = input()
    list = str.split(" ")
    list.sort()
    for i in range(0, size - math.floor(size/2)):
        sentinel = 0
        if(list[i] == list[i + math.ceil(size/2) - 1]):
            print(list[i])
            sentinel = 1
            break
    if(sentinel == 0):
        print(-1)