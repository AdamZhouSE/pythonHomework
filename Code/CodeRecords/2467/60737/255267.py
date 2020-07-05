t = int(input())
while t:
    cmd = [int(n) for n in input().split()]
    arrm = [int(n) for n in input().split()]
    arrn = [int(n) for n in input().split()]
    m = cmd[0]
    n = cmd[1]
    k = cmd[2]
    arr = []
    for i in arrm:
        arr.append(i)
    for j in arrn:
        arr.append(j)
    arr.sort()
    print(arr[k-1])
    t -= 1
    