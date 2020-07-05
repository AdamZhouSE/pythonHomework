n = int(input())
if n == 0:
    print("False")
else:
    a = str(n**0.5).split(".")
    if a[1] == '0':
        print("True")
    else:
        print("False")