test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    x = int(input())
    array = [int(x) for x in array]
    array.sort()
    sentinel = 0
    for j in range(len(array)-3):
        for k in range(j+1,len(array)-2):
            for m in range(k+1,len(array)-1):
                for t in range(m+1,len(array)):
                    if array[j]+array[k]+array[m]+array[t] == x:
                        sentinel = 1
    if sentinel == 0:
        print(0)
    else:
        print(1)
