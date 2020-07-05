t = int(input())
for i in range(t):
    arr = input()
    arr = input()
    arr = [int(k) for k in arr.split(" ")]
    arr.sort()
    if arr.__len__() % 2 == 1:
        print(arr[arr.__len__() // 2 - 1])
    else:
        print((arr[arr.__len__() // 2] + arr[arr.__len__() // 2 + 1]) // 2)
