def isNumber( s: str) -> bool:
    try:
        float(s)
        return True
    except:
        return False

a = input()
print(isNumber(a))