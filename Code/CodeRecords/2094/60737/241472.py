def is_number(s):
    s = s.strip()
    if len(s)<1:
        return False
    i = 0
    if len(s)==1:
        return s.isdigit()
    numstr = list(s)
    if (numstr[i] == '+') or (numstr[i] == '-'):
        i += 1
    pcount = 0
    dcount = 0
    while (numstr[i].isdigit() or numstr[i] == '.') and (i<len(numstr)-1):
        if numstr[i] == '.':
            pcount += 1
        else:
            dcount += 1
        i += 1
    if pcount>1 or dcount<1:
        return False
    if numstr[i] == 'e' and i<len(numstr)-1:
        dcount = 0
        i += 1
        if (numstr[i] == '+') or (numstr[i] == '-'):
            i += 1
        while numstr[i].isdigit() and i<len(numstr)-1:
            dcount += 1
            i += 1
        if dcount<0:
            return False
    return numstr[i].isdigit()


if __name__ == "__main__":
    s = input()
    print(is_number(s))
