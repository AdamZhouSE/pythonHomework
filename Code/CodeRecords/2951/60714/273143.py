from math import log

a = input()
b = input()
ans1 = 0
for i in range(len(a) - 1, -1, -1):
    ans1 += int(a[i]) * pow(2, len(a) - i - 1)
ans2 = 0
for i in range(len(b) - 1, -1, -1):
    ans2 += int(b[i]) * pow(3, len(b) - i - 1)
for i in range(len(a) - 1, -1, -1):
    m = ans1
    if a[i] == "0":
        ans1 += pow(2, len(a) - i - 1)
    else:
        ans1 -= pow(2, len(a) - i - 1)
    if ans1 < ans2:
        temp = ans2 - ans1
        if temp % 2 == 0:
            temp /= 2
            j = log(temp, 3)
            if j == int(j):
                j = int(j)
                if b[len(b) - int(j) - 1] == "2":
                    print(ans1, end="")
                    break
        else:
            j = log(temp, 3)
            if j == int(j):
                j = int(j)
                if b[len(b) - int(j) - 1] != "0":
                    print(ans1, end="")
                    break
    elif ans1 > ans2:
        temp = ans1 - ans2
        if temp % 2 == 0:
            temp /= 2
            j = log(temp, 3)
            if j == int(j):
                j = int(j)
                if b[len(b) - int(j) - 1] == "0":
                    print(ans1, end="")
                    break
        else:
            j = log(temp, 3)
            if j == int(j):
                j = int(j)
                if b[len(b) - int(j) - 1] != "2":
                    print(ans1, end="")
                    break
    ans1 = m
