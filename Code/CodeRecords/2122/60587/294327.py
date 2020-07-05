x = int(input())
y = int(input())
z = int(input())
global hcf
if x + y < z:
    print("False")
else:
    smaller = min(x, y)
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    if z % hcf == 0:
        print("True")
    else:
        print("False")
