n = int(input())
arr = []
count = 1
start = 0
for i in range(1000):
    start += 1
    for j in range(count):
        arr.append(start + 2 * j)
    start = arr[-1]
    count += 1
print(arr)
for i in range(n):
    index = int(input())
    print(arr[index])
