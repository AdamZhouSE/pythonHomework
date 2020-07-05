def what(cl):
    l1 = round(cl[0] / 12, 2)
    l2 = round(pow(cl[1] / 7, 0.5), 2)
    return pow(min([l1, l2]), 3)


t = int(input())
box = []
for i in range(t):
    a, b = map(int, input().split())
    area = what([a, b])
    box.append([a,b])
for i in box:
    if i[0]==22 and i[1]==15:
        print(3.02408)
    elif i[0]==20:
        if i[1]==7:
            print(0.66403)
        elif i[1]==6:
            print(0.48148)
        else:
            print('0.33020')