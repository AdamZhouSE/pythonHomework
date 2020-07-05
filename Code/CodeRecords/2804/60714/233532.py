num = input().split("+")
num.sort()
print(num[0], end="")
for i in range(1, len(num)):
    print("+" + num[i], end="")
