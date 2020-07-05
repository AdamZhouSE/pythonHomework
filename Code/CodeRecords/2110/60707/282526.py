num = int(input())
if num < 1:
    print("False")
else:
    while num % 2 == 0:
        num = int(num / 2)
    while num % 3 == 0:
        num = int(num / 3)
    while num % 5 == 0:
        num = int(num / 5)
    if num == 1:
        print("True")
    else:
        print("False")