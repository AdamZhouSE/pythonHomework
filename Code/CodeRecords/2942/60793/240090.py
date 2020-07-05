input()
ls = list(input().split(" "))
maxNum = 0
for i in range(0, len(ls)):
    temp = int("".join(ls))
    if temp > maxNum:
        maxNum = temp
    ls = ls[1:] + ls[0]
print(maxNum, end="")