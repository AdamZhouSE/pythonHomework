up = int(input())
down = int(input())
result = []
if up >= down:
    result.append(int(up/down))
    up = up % down
    if up != 0:
        result.append(".")
else:
    result.append(0)
    result.append(".")
while up != 0:
    last = up
    up *= 10
    result.append(int(up/down))
    up = up % down
    if up == last:
        result.insert(len(result)-1, "(")
        result.append(")")
        break
for i in range(len(result)):
    print(result[i], end="")
print()
