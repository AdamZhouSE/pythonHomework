t = int(input())
for i in range(t):
    arr = input()
    arr = [int(k) for k in arr.split(" ")]
    k = arr[1]
    arr = input()
    arr = [int(k) for k in arr.split(" ")]
    arr.sort()
    count = 0
    for j in arr:
        if k - j >0:
            count += 1
            k -= j
        else:
            break
    print(count)