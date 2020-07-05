N = int(input())
s = input()
scores = 0
if s == "F"*N:
    print(0, end="")
    exit()
for ch in s:
    if ch == "A": scores += 4
    elif ch == "B": scores += 3
    elif ch == "C": scores += 2
    elif ch == "D": scores += 1
print("{:.14f}".format(scores/N), end="")
