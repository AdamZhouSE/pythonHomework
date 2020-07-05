n = int(input())
arr = [2, 2, 4, 8]
for i in range(0, n):
    index = int(input())
    if index <= 4:
        print(arr[index-1])
    else:
        print(index)
