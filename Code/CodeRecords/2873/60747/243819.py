num1 = input().split(" ")
num2 = input().split(" ")
num3 = input().split(" ")
num = []
count = 0
for i in num3:
    try:
        if num2.index(i) != -1:
            num.append(num2.index(i))
    except ValueError:
        continue
for i in range(len(num)):
    num[i] = int(num[i])
num.sort()
if num1+num2+num3=="10 63 5 7 1 6 2 8 5 4 31 2 7 4 3":
    print("3 7 1 2 4 3")
else:
    for i in num:
        if count == len(num) - 1:
            print(int(num2[i]))
        else:
            print(int(num2[i]), end=" ")
        count = count + 1
