def isNumber(s: str) :
    try:
        num = float(s)
        return True
    except:
        return False
s=input()
print(isNumber(s))