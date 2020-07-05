t = int(input())
c = int(input())
x = (t - 2*c) / 2
y = c - x
if x - int(x) == 0 and y - int(y) == 0 and x>=0 and y>=0:
    print([int(x), int(y)])
else:
    print([])