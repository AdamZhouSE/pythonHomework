t = int(input())
for i in range(t):
    n = int(input())
    arr = input()
    arr = [int(k) for k in arr.split(" ")]
    arr.sort()
    sum = 0
    while arr.__len__() > 1:
        tmp = arr[0] + arr[1]
        sum += tmp
        arr.pop(0)
        arr.pop(0)
        arr.append(tmp)
        arr.sort()
    print(sum)
