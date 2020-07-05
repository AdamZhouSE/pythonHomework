a = float(input())
b = int(input())
re = 1.00
if b >= 0:
    for i in range(b):
        re *= a
    print("%.5f" % re)
else:
    for i in range(-b):
        re *= a
    print("%.5f" % (1 / re))