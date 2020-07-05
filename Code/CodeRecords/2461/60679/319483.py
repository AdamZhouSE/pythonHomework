str = input()
location = 0
arr = str.split(",")
arr = [int(arr[i]) for i in range(len(arr))]
arr.sort()
print(arr[0])