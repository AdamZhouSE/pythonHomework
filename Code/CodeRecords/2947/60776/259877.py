def yi(yuanwen,charu):
    return yuanwen+charu

def er(yuanwen,qi,length):
    return yuanwen[qi:qi+length]

def san(yuanwen,weizhi,str):
    return yuanwen[0:weizhi]+str+yuanwen[weizhi:len(yuanwen)]

def si(yuanwen,str):
    if str not in yuanwen :
        return -1
    else:
        for i in range(0,len(yuanwen)):
            if yuanwen[i:i+len(str)]==str:
                return i

if __name__ == "__main__":
    a=int(input())
    yuanwen=input()
    for i in range(0,a):
        list=input().split(' ')
        if(list[0]=="1"):
            yuanwen=yi(yuanwen,list[1])
            print(yuanwen)
        elif(list[0]=="2"):
            b=int(list[1])
            c=int(list[2])
            yuanwen=er(yuanwen,b,c)
            print(yuanwen)
        elif(list[0]=="3"):
            b=int(list[1])
            yuanwen=san(yuanwen,b,list[2])
            print(yuanwen)
        else:
            x=si(yuanwen,list[1])
            print(x)
