#08
N = int(input())
s = input()
count = 0
for c in s:
    if c == "A":
        count += 4
    if c == "B":
        count += 3
    if c == "C":
        count += 2
    if c == "D":
        count += 1
if count == 0:
    print(0,end="")
else:
    print(format((count / N), '.14f'), end="")