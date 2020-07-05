#11
parentheses = []
s = input()
for c in s:
    if c == ')' or c == '(':
        parentheses.append(c)
total = 0
for item in parentheses:
    if total < 0:
        break
    if item == '(':
        total += 1
    else:
        total -= 1
if total == 0:
    print("YES",end="")
else:
    print("NO",end="")



