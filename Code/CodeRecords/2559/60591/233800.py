def Iso(string):
    string = list(string)
    string.sort()
    string = "".join(string)
    pre = string[0]
    for m in range(1,len(string)):
        if(string[m]==pre):
            return True
        else:
            pre = string[m]
    return False

number = eval(input())
while(number>0):
    temp = Iso(input())
    if(temp):
        print(0)
    else:
        print(1)
    number = number - 1