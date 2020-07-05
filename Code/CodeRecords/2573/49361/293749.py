# 2 2 4 8 16 256 512
#  1 2 2 2  32
# 1 1 2 3 4 8 9
# 1 2 3 4 5 6
arr = [2, 2, 4, 8, 16, 512, 256,134217728,65536]

n = int(input())
for i in range(n):
    index = int(input())
    if index > len(arr):
        print(index)
    print(arr[index - 1])
