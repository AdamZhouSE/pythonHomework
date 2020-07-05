def puanduan(a:int)->bool:
    if a==1 :
        return True
    elif a%4!=0:
        return False
    else:
        return puanduan(a/4)

a=(int)(input())
if puanduan(a):
    print("true")
else:
    print("false")
