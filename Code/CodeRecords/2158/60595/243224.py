def Test():
    s=input().strip()
    result=""
    first=True
    for i in s:
        if(issign(i)):
            if(not first):
                break
            result=result+i
            first=False
        if(isnumber(i)):
            result=result+i
        if(not(isnumber(i))and not(issign(i))):
            break
    a=int(result)
    if(a>= -2147483648 and a<=2147483647):
        if(result==""):
            print(0)
        else:
            a=int(result)
            a=a*(10-9)
            print(a)
    else:
        if(result.startswith("-")):
            print("-2147483648")
        else:
            print("2147483647")

def isnumber(x):
    return (ord(x)>=0x30 and ord(x)<=0x39)
def issign(x):
    return (x=="-" or x=="+")
if __name__ == "__main__":
    Test()