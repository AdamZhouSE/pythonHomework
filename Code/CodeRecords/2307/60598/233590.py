num = int(input())
# 输入的测试用例的数量


def find(array):
    array = sorted(array)
    pre = array[0]
    count = 1
    for index in range(1, len(array)):
        if array[index] == pre:
            count = count+1
            pre = array[index]
        else:
            count = 1
            pre = array[index]
        if count > len(array)/2:
            return array[index]
    return -1


for i in range(num):
    length = int(input())
    arrays = map(int, input().split(" "))
    print(find(arrays))

