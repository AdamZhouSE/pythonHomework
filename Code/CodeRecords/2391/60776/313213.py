a=int(input())
zongren=[]
for i in range(0,a):
    zongren.append(input())
yidian=[]
a=int(input())
for i in range(0,a):
    b=input()
    if b in zongren:
        if b not in yidian:
            print("OK")
            yidian.append(b)
        else:
            print("REPEAT")
    else:
        print("WRONG")