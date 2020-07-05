while True:
    strin=input()
    if(strin=='!'):
        break;
    strout=''
    for s in strin:
        if(s.islower()):
            strout=strout+chr(ord('z')-ord(s)+ord('a'))
        elif(s.isupper()):
            strout=strout+chr(ord('Z')-ord(s)+ord('A'))
        else:
            strout=strout+s
    print(strout)