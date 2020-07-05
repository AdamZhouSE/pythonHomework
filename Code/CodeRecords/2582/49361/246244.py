s1 = input().split(",")
s2 = input().split(",")
arr1 = []
arr2 = []
for item in s1:
    arr1.append(int(item))
for item in s2:
    arr2.append(int(item))
result = 0
for indexi in range(len(arr1)):
    for indexj in range(len(arr2)):
        result = max(result, abs(arr1[indexi] - arr1[indexj]) + abs(arr2[indexi] - arr2[indexj]) + abs(indexi - indexj))
print(result)