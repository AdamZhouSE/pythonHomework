n = int(input())
ans = 0
for char in input():
    if char == 'A':
        ans += 4
    elif char == 'B':
        ans += 3
    elif char == 'C':
        ans += 2
    elif char == 'D':
        ans += 1
if ans == 0:
    print(0, end="")
else:
    print("%.14f" % (ans / n), end="")
