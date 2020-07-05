input()
ls = list(input().split(" "))
maxNum = 0
for i in range(0, len(ls)):
    temp = int("".join(ls))
    if temp > maxNum:
        maxNum = temp
print(maxNum, end="")