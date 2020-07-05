a = int(input())
if a == 0:
    print(0)
else:
    i = a % 9
    if i == 0:
        print(9)
    else:
        print(i)