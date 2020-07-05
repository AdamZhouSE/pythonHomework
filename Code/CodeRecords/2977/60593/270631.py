while(True):
    ss=input()
    ret=['']*len(ss)
    if(ss=='!'):
        break
    for i in range(len(ss)):
        if(ss[i].isalpha()):
            if(ss[i].islower()):
                ret[i]=chr(ord('z')-(ord(ss[i])-ord('a')))
            else:
                ret[i]=chr(ord('Z')-(ord(ss[i])-ord('A')))
        else:
            ret[i]=ss[i]
    print(''.join(ret))