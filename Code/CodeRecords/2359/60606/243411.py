test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    array.sort()
    sentinel = 0
    num = 0 
    for j in range(0,len(array)-2):
        for k in range(j+1,len(array)-1):
            sum = array[j]+array[k]
            for m in range(k+1,len(array)):
                if array[m] == sum:
                    sentinel = 1
                    num += 1
    if sentinel == 0:
        print(-1)
    else:
        print(num)