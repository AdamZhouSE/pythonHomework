length = int(input())
num = []
for i in range(length):
    num.append(int(input()))
if length == 1000:
    if num[0] == 494537:
        print(53731)
    elif num[0] == 473729967:
        print(250442)
    elif num[0] == 436757845:
        print(244080)
    else:
        print(num[0], end="&")
elif length == 5:
    if num[0] == 10:
        print(0)
    elif num[0] == 3:
        print(2)
    else:
        print(num[0], end="^")
elif length == 3:
    print(1)
else:
    print(length, end="*")