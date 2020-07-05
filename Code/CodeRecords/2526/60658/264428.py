arr1 = input()[1:-1].split(",")
arr2 = input()[1:-1].split(",")
while "null" in arr1:
    arr1.remove("null")
while "null" in arr2:
    arr2.remove("null")
while "" in arr1:
    arr1.remove("")
while "" in arr2:
    arr2.remove("")
arr1 = list(map(int,arr1))
arr2 = list(map(int,arr2))
arr1.extend(arr2)
arr1.sort()
print(arr1)