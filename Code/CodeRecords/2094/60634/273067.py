def legal(ch, eCh, poiCh, negCh, posCh):
    if ch <= '9' and ch >= '0':
        return True
    elif ch == 'e' and eCh == 1:
        return True
    elif ch == '.' and poiCh == 1:
        return True
    elif ch == '-' and negCh == 1:
        return True
    elif ch == '+' and posCh == 1:
        return True
    else:
        return False
    

def judge(s):
    eCh = 0
    poiCh = 0
    negCh = 1
    posCh = 1
    if len(s) == 1:
        return legal(s[0],0,0,0,0)
    if not legal(s[0],eCh,poiCh,negCh,posCh):
        return False
    else:
        negCh = 0
        posCh = 0
        if s[0] != '+' and s[0] != '-':
            poiCh = 1
            eCh = 1
    if not legal(s[1],eCh,poiCh,negCh,posCh):
        return False
    eCh = 1
    poiCh = 1
    i = 2
    while i < len(s):
        if legal(s[i],eCh,poiCh,negCh,posCh):
            if s[i] == '.':
                poiCh = 0
            elif s[i] == 'e':
                eCh = 0
                poiCh = 0
                negCh = 1
                posCh = 1
                break
        else:
            return False
        i += 1
    if negCh == 1:#and posCh == 1:
        i += 1
        if i == len(s):
            return False
        if not legal(s[i],eCh,poiCh,negCh,posCh):
            return False
        else:
            negCh = 0
            posCh = 0
            if s[i] != '+' and s[i] != '-':
                poiCh = 1
                eCh = 1
        i += 1
        if not legal(s[i],eCh,poiCh,negCh,posCh):
            return False
        poiCh = 1
        i += 1
        while i < len(s):
            if legal(s[i],eCh,poiCh,negCh,posCh):
                if s[i] == ".":
                    poiCh = 0
            else:
                return False
            i += 1
    return True
        
        
#main-----
s = input()
print(judge(s))
