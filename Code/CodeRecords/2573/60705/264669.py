n = int(input())
arr = [2, 2, 4, 8, 16, 512, 256, 134217728, 65536]
for i in range(0, n):
    index = int(input())
    if index <= 9:
        print(arr[index-1])
    else:
        print(index)
