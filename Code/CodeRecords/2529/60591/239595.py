def find(num):
    basic = 1
    num = list(num)
    num.sort()
    num = "".join(num)
    while(len(str(basic)) <= len(num)):
        temp = str(basic)
        temp = list(temp)
        temp.sort()
        temp = "".join(temp)
        if(temp == num):
            return True
        else:
            basic *= 2
    return False

if(find(input())):
    print("true")
else:
    print("false")