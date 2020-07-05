x = int(input())
y = int(input())
z = int(input())
possible = [x, y, abs(x - y)]
if max(x, y) % min(x, y) != 0:
    possible.append(min(x, y) - max(x, y) % min(x, y))
diff1 = z - min(x, y)
diff2 = max(x, y) - z
if (diff1 in possible or diff2 in possible) and x <= z <= y:
    print(True)
else:
    print(False)
