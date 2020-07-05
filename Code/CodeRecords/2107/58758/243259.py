num = int(input())
factor = 1
while factor < num:
    factor *= 2
if num < factor:
    print(False)
else:
    print(True)
