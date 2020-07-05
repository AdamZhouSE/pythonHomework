inst=input()
x = 0
y = 0
c = 0
inst=inst*4
inst=list(inst)
for i in inst:
    if i == 'G':
        if c == 0:
            y += 1
        elif c == 1:
            y -= 1
        elif c == 2:
            y -= 1
        else:
            x += 1
    elif i == 'L':
        if c == 3:
            c = 0
        else:
            c += 1
    elif i == 'R':
        if c == 0:
            c = 3
        else:
            c -= 1
if x == 0 and y == 0:
    print("True")
else:
    print("False")