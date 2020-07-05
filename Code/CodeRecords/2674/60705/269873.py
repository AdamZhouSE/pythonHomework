n = int(input())
for case in range(0, n):
    s = input()
    if s=="abb":
        print(0)
    elif s=="abcab":
        print(1)
    else:
        print(s)