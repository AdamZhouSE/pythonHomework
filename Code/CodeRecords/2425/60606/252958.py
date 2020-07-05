import math
test_num = int(input())
for i in range(test_num):
    line = input().split(" ")
    n = int(line[0])
    x = int(line[1])
    array = input().split(" ")
    array = [int(x) for x in array]
    minus = 999
    store = 0
    for j in array:
        if math.fabs(j-x) < minus:
            store = j
            minus =  math.fabs(j-x)
        elif math.fabs(j-x) == minus:
            store = max(store,j)
    print(store)
