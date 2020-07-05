num = input().split("+")
num.sort()
for i in range(0, len(num) - 1):
    print(num[i] + "+", end="")
print(num[len(num) - 1])
