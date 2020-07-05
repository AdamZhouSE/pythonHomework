num = int(input())
factor = 1
while factor < num:
    factor *= 3
if factor == num:
    print(True)
else:
    print(False)
