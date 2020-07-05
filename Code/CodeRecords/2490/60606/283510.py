import numpy as np
array1 = input()[1:-1].split(",")
array2 = input()[1:-1].split(",")
result = []
for item1 in array1:
    for item2 in array2:
        if item1 == item2:
            result.append(item1)
result.sort()
result = [int(x) for x in result]
temp = np.array(result)
temp = np.unique(temp)
out = []
for item in temp:
    out.append(item)
print(out)