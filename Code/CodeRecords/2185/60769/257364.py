import math

num = int(input())
for j in range(num):
    n = int(input())
    m = math.ceil(math.log(n + 2, 2) - 1)
    res = ""
    bins = str(bin(int(-math.pow(2, m) + 2 + n - 1)))[2:]
    # print(bins)
    for i in range(len(bins)):
        if bins[-1 - i] == "1":
            res = "7" + res
        else:
            res = "4" + res
    res = "4"*(m-len(bins))+res
    print(res)
