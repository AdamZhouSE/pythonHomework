def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

num = int(input())
for i in range(num):
    numList=list(input())
    AList=list(input())
    BList=list(input())
    All=list(set(AList+BList))

    res=0
    for c in All:
        if is_number(c):
            res=res+1
    print(res)