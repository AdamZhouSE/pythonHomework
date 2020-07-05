def judge(array):
    max_men = max(array)
    list = []
    for i in range(len(array)):
        if array[i] == max_men:
            list.append(i)
    return list


number = input().split()
array = []
max_length = 0
for i in range(int(number[0])):
    temp = input().split()
    array.append([int(temp[0]), int(temp[1]) - 1, int(temp[2])])
    if int(temp[1]) > max_length:
        max_length = int(temp[1])
array.sort()
cow = [int(number[1])] * max_length
count = 0
picture = []
for i in range(max_length):
    picture.append(i)
for i in range(len(array)):
    cow[array[i][1]] = cow[array[i][1]] + array[i][2]
    result = judge(cow)
    if result != picture:
        picture = result[:]
        count = count + 1
print(count, end='')
