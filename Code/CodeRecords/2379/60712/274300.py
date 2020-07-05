str1 = list(input())
x = 0
y = 0
dire = 0
bl=False
for j in range(1,20):
    for i in range(len(str1) * j):
        if str1[i % len(str1)] == 'G':
            if (dire+400) % 4 == 0:
                y += 1
            elif (dire+400) % 4 == 1:
                x += 1
            elif (dire+400)% 4 == 2:
                y = y - 1
            elif (dire+400)%4==3:
                x = x - 1
        elif str1[i % len(str1)] == 'L':
            dire -= 1
        else:
            dire += 1
    if x == 0 and y == 0:
        bl=True
        break
if bl:
    print('True')
else:
    print('False')

       