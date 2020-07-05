tomatoSlices=int(input())
cheeseSlices=int(input())
s = (4 * cheeseSlices - tomatoSlices) / 2
b = (tomatoSlices - 2 * cheeseSlices) / 2
if s >= 0 and b >= 0 and s == int(s) and b == int(b):
    print([int(b), int(s)])
else:
    print("[]")