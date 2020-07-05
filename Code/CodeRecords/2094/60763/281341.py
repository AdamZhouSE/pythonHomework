def isNumber1( s: str) -> bool:
    import re
    s = s.strip()
    if s == '':
        return False

    a = re.match('[+-]?(\d+\.?|\.\d+)\d*(e[+-]?\d+)?', s)

    if a and a.group(0) == s:
        return True
    else:
        return False


def isNumber( s: str) -> bool:
    try:
        float(s)
        return True
    except:
        return False


a = input()
print(isNumber1(a))