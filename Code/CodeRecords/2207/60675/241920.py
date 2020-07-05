def isAcc(n,m):
    value = (2 * n) / m
    string = str(value)
    s = string.split(".")
    if int(s[1]) == 0:
        if value == 2:
            return 0
        else:
            if int(value) >= m+1:
                return 1
            else:
                return 0
    else:
        return 0

num = int(input())
for i in range(num):
    a = input()
    pair = a.split(" ")
    print(isAcc(int(pair[0]), int(pair[1])))