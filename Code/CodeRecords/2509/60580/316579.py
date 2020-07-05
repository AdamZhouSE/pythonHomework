length = int(input())
array = input().split()
for i in range(len(array)):
    array[i] = int(array[i])
num = int(input())
for i in range(num):
    temp = input().split()
    if temp[0] == "add":
        array.append(int(temp[1]))
        array.sort()
    else:
        print(array[int((len(array) + 1) / 2) - 1])
