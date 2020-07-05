a = int(input())
b = int(input())
c = int(input())

def move():
    z = max(a, b, c)
    x = min(a, b, c)
    y = a + b + c - x - z

    if y - x == 1 and z - y == 1:
        return [0, 0]
    elif y - x <= 2 or z - y <= 2:
        return [1, y - x + z - y - 2]
    else:
        return [2, y - x + z - y - 2]

print(move())
