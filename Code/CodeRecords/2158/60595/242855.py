def Test():
    s=input().strip()
    result=""
    begin=False
    for i in s:
        if(isnumber(i) or issign(i)):
            result=result+i
            begin=True
        if(begin and not(isnumber(i))):
            break
    try:
        print(result)
    except:
        if(result.startswith("-")):
            print("-2147483648")
        else:
            print("2147483647")

def isnumber(x):
    return (x>=0x31 and x<=0x39)
def issign(x):
    return (x=="-" or x=="+")
if __name__ == "__main__":
    Test()