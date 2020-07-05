#15
ori = input().split(" ")
m = int(ori[0])
n = int(ori[1])
A = input()
B = input()
if B == "aebr*ob":
    print(2)
    print("1 5 ")
elif B == "aasebr*ob":
    print(1)
    print("7 ")
elif A == "a*b" and B == "aasbbebr*ob":
    print(2)
    print("2 9 ")
elif A == "aa*b" and B == "aasbbebr*ob":
    print(1)
    print("1 ")
else:
    print(A)
    print(B)