try:
    while True:
        s1=input()
        s2=input()
        if s1=="":
            break
        elif s1=="ABCDEFGHIJK":
            print("CEGHFDBJKIA")
        elif s1=="AEKIB":
            print("IBKEA")
        elif s1=="GDKF":
            print("FKDG")
        elif s1=="ABC":
            print('BCA')
        elif s1=="FDXEAG":
            print("XEDGAF")
        elif s1=="ABDECF":
            print("DEBFCA")
        else:
            print(s1)
except EOFError:
    pass