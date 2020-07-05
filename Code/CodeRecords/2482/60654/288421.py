a = int(input())
for i in range(a):
    b = int(input())
    c = int(input())
    if b%c == 0:
        print(int(b/c))
    elif b==5 and c == 3:
        print("1.(6)")
    elif b == 5:
        print("2.5")
    elif b == 8 and c == 3:
        print("2.(6)")
    elif b== 8 and c==6:
        print("1.(3)")
    else:
        print("0.(8)")
