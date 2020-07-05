arr=input().replace("[","").replace("]","").split(",")
arr.sort()
print(arr[int(len(arr)/2)])