n = int(input())
string = input()
summ = 0
for i in range(0, n):
    a = string[i]
    if a == "A":
        summ += 4
    elif a == "B":
        summ += 3
    elif a == "C":
        summ += 2
    elif a == "D":
        summ += 1
if summ == 0:
    print(0, end="")
else:
    print("%.14f" % (summ / n), end="")