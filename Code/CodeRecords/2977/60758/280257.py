def getReverse(a):
    asc=ord(a)
    if(asc>=65 and asc<=90):
        return chr(90-(asc-65))
    elif(asc>=97 and asc<=122):
        return chr(122-(asc-97))
    else:
        return a


string=""
while(True):
    string=input()
    if(string=='!'):
        break
    out=""
    for i in string:
        out+=getReverse(i)
    print(out)