t = int(input())
for i in range(t):
    l = input()
    arr = input()
    arr = [int(k) for k in arr.split(" ")]
    arr.sort()
    if arr[-1] % arr[0] == 0:
        print(arr[-1])
    else:
        print(arr[0]*arr[-1])
