str = input()
str = str[1:len(str)-1]
arr = str.split(",")
arr = [int(arr[i]) for i in range(len(arr))]
arr.sort()
print(arr)