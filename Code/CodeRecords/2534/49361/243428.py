arrays = input().replace("[", "").replace("]", "").split(",")
result = []
for each in arrays:
    each = int(each)
    result.append(each)
for indexi in range(len(result)):
    for indexj in range(indexi + 1, len(result)):
        if result[indexi] > result[indexj]:
            temp = result[indexi]
            result[indexi] = result[indexj]
            result[indexj] = temp
print(result)
