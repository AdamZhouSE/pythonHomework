import math
# question 13
def func13():
    for _ in range(0, eval(input())):
        n, arr = eval(input()), input().split()
        po, res, val = [0, 0], ["N", "W", "S", "E"], 0
        for i in range(0, n * 2, 2):
            if arr[i] == "D":
                val = val + 2 if val + 2 < 4 else (val + 2) % 4
            elif arr[i] == "L":
                val = val + 1 if val + 1 < 4 else 0
            elif arr[i] == "R":
                val = val - 1 if val - 1 >= 0 else 3

            if val == 0:
                po[1] += int(arr[i + 1])
            elif val == 1:
                po[0] -= int(arr[i + 1])
            elif val == 2:
                po[1] -= int(arr[i + 1])
            else:
                po[0] += int(arr[i + 1])
        ans = int(math.sqrt(pow(po[0], 2) + pow(po[1], 2)))
        print("%d %s" % (ans, res[val]))


func13()

