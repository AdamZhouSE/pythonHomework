l = list(input().split("\n"))
if len(l[0]) != len(l[1]):
    print(1)
else:
    if l[0] == l[1]:
        print(2)
    elif l[0].lower() == l[1].lower():
        print(3)
    else:
        print(4)
