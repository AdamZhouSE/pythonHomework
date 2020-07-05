n=int(input(""))
Astate=0
Bstate=0
for i in range(n):
    ID,success,fail=map(int,input("").split(" "))
    if ID==1:
        Astate=Astate+success-fail
    else:
        Bstate=Bstate+success-fail
if Astate>=0:
    print("LIVE")
else:
    print("DEAD")
if Bstate>=0:
    print("LIVE")
else:
    print("DEAD")
