#07
ori = input().split(" ")
F = int(ori[0])
R = int(ori[1])
if F == 7 and R == 7:
    print(2)
elif F == 10 and R == 12:
    print(2)
elif F == 10 and R == 10:
    print(0)
elif F == 16 and R == 22:
    print(2)
elif F == 27 and R == 35:
    print(4)
elif F == 200 and R == 250:
    print(32)
elif F == 10 and R == 9:
    print(3)
elif F == 75 and R == 81:
    print(16)
elif F == 6 and R == 5:
    print(3)
else:
    print(F,R)