def findSecond(item):
    return item[1]


number = input().split()
array = input().split()
for i in range(int(number[0])):
    array[i] = int(array[i])
for i in range(int(number[1])):
    temp = input().split()
    start = int(temp[0]) - 1
    end = int(temp[1])
    rank = int(temp[2]) - 1
    list = array[start:end]
    list.sort()
    print(list[rank])
