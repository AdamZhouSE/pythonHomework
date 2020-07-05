def count(array):
    list = []
    for i in range(len(array) - 1):
        acount = 0
        num = i
        while num < len(array) - 1 and array[num] + array[num + 1] == 1:
            acount = acount + 1
            num = num + 1
        list.append(acount)
    return max(list) + 1


number = input().split()
array = [0 for _ in range(int(number[0]))]
list = []
for i in range(int(number[1])):
    temp = int(input())
    array[temp - 1] = 1 - array[temp - 1]
    print(count(array))
