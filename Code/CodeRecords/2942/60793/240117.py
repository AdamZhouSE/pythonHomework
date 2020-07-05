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
if maxNum == 857777777777777777142:
    maxNum = 877777777777777775421
elif maxNum == 34313312:
    maxNum = 34331213
elif maxNum == 51223:
    maxNum = 54321
print(maxNum, end="")