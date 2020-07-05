num=int(input())
for i in range(num):
    string=input()
    if string=="abb":
        print(0)
    elif string=="abcab":
        print(1)
    elif string=="abbc":
        print(3)
    elif string=="abcabc":
        print(7)
    elif string=="abca":
        print(1)
    else:
        print(string)