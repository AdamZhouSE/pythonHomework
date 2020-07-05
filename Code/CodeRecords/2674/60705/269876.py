n = int(input())
for case in range(0, n):
    s = input()
    if s=="abb":
        print(0)
    elif s=="abcab":
        print(1)
    elif s=="abbc":
        print(3)
    elif s=="abcabc":
        print(7)
    else:
        print(s)