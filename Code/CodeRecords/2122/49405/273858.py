x = int(input())
y = int(input())
z = int(input())
if x == y:
    print(x == z)
else: print(z % (y - x) == 0)