import math
def so(n,arr):
    point, con, temp = [0, 0], ["N", "W", "S", "E"], 0
    for i in range(0, n * 2, 2):
        if arr[i] == "D":
            temp = temp + 2 if temp + 2 < 4 else (temp + 2) % 4
        elif arr[i] == "L":
            temp = temp + 1 if temp + 1 < 4 else 0
        elif arr[i] == "R":
            temp = temp - 1 if temp - 1 >= 0 else 3

        if temp == 0:
            point[1] += int(arr[i + 1])
        elif temp == 1:
            point[0] -= int(arr[i + 1])
        elif temp == 2:
            point[1] -= int(arr[i + 1])
        else:
            point[0] += int(arr[i + 1])
    rr = str(int(math.sqrt(pow(point[0], 2) + pow(point[1], 2))))
    return rr+" "+con[temp]
n = eval(input())
for i in range(0,n):
    print(so(eval(input()),input().split(' ')))