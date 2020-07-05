arr1 = input().strip("[]").split(",")
arr1 = list(map(int,arr1))
arr2 = input().strip("[]").split(",")
arr2 = list(map(int,arr2))
arr3 = []
for i in arr2:
    for j in range(arr1.count(i)):
        arr1.remove(i)
        arr3.append(i)
arr1.sort()
print(arr3+arr1)