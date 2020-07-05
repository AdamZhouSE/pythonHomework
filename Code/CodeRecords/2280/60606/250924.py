test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    array.sort()
    sum1 =(1+n)*n/2
    sum2 = 0
    for i in range(len(array)):
        sum2 += array[i]
    print(int(sum1-sum2))
