def joseph(n, k):
    arr = [i+1 for i in range(n)]
    index = k-1
    while len(arr) > 1:
        arr.remove(arr[index])
        index += k-1
        if index >= len(arr):
            index = index % len(arr)
    return arr[0]


result = []
for i in range(int(input())):
    a = input().split()
    result.append(joseph(int(a[0]), int(a[1])))
for i in range(len(result)):
    print(result[i])