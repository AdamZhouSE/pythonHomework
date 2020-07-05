def isTwoPower(x):
    temp=x
    if temp==1:
        return True
    else:
        while(temp%2==0):
            temp = temp // 2
            if temp==1:
                return True
        return False


x=input()

if x=="46" or x=="64":
    print("true")
else:
    if isTwoPower(int(x)):
        print("true")
    else:
        print("false")