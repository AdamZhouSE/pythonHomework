length = int(input())
num = input()
count = 0
for s in num:
    if s == "0":
        count += 1
print("1"+count*"0", end="")
