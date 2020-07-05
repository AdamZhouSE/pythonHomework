a = float(input())
b = int(input())
f = 1
if b == 0:
    f = 1
elif b>0:
    for i in range(b):
        f = f*a
else:
    for i in range(abs(b)):
        f = f/a
print("%.5f"%f)