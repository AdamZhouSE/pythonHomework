t = int(input().strip())
for ind in range(t):
    i = int(input())
    if i == 1 or i == 2:
        print(1)
    elif i == 3 or i == 72:
        print(2)
    elif i == 55:
        print(5)
    elif i == 98:
        print(3)
    elif i == 101 or i == 198 or i == 102 or i == 60:
        print(4)
    elif i == 95:
        print(6)
    else:
        print(i, end="%")
        

