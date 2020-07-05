input()
ls = list(input().split(" "))
maxNum = 0
for i in range(0, len(ls)):
    temp = int("".join(ls))
    if temp > maxNum:
        maxNum = temp
    newLs = ls[1:]
    newLs.append(ls[0])
    ls = newLs
print(maxNum, end="")