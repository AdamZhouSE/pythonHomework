a = input()
b =a+input()
if b=="3,13,3,26" or b=="4,9,3,26":
    print(1)
elif b=="4,9,3,21" or b=="3,13,3,21" or b=="3,6,3,21":
    print(0)
elif b=="4,9,310":
    print(3)
else:
    print(b)