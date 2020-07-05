#对每一列去找，向前向后找到小的为止
test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    result = []
    for j in range(n):
        left = 0
        right = 0
        for k in range(j+1,len(array)):
            if array[k] >= array[j]:
                right +=1
            else:
                break
        for k in range(j-1,-1,-1):
            if array[k] >= array[j]:
                left +=1
            else:
                break
        temp = (1+right+left)*array[j]
        result.append(temp)
    result.sort()
    print(result[len(result)-1])
        