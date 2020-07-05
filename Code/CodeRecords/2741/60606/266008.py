array = input()[1:-1].split(",")
array = [int(x) for x in array]
length = 1
result = []
for i in range(1,len(array)):
    if array[i-1] < array[i]:
        length += 1
    else:
        result.append(length)
        length = 1
max = 0
for i in result:
    if max < i:
        max = i

print(max)