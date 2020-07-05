n = int(input())
arr = [2, 2, 4, 8, 16]
for i in range(0, n):
    index = int(input())
    if index <= 5:
        print(arr[index-1])
    else:
        print(index)
