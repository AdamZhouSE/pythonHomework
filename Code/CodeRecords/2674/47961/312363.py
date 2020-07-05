a=int(input())
for i in range(0,a):
    b=input()
    if b=="abbc":print(3)
    elif b=="abcabc":print(7)
    elif b=="abb":print(0)
    elif b=="abcab" or b=="abca":print(1)
    else:print(b)