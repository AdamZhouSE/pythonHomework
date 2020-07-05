def isValid(string):
    temp = []
    for x in string:
        if x in "([{":
            temp.append(x)
        else:
            if(len(temp) == 0):
                return False
            back = temp[-1]
            del temp[-1]
            if(x == "("):
                if(back != ")"):
                    return False
            elif(x == "["):
                if(back != "]"):
                    return False
            elif(x == "{"):
                if(back != "}"):
                    return False
    if(len(temp)==0):
        return True
    else:
        return False

n = eval(input())
while(n != 0):
    n = n - 1
    if(isValid(input())):
        print("balanced")
    else:
        print("not balanced")