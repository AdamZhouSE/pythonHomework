array1 = input()[1:-1].split(",")
array2 = input()[1:-1].split(",")
result = []
for item1 in array1:
    for item2 in array2:
        if item1 == item2:
            result.append(item1)
result.sort()
print(result)