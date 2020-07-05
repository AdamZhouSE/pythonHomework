# map.get(c,0)

def isAnagram(s,t):
    if len(s)!=len(t): return False
    setS=set(s)    ####
    if setS == set(t):
        for c in setS:   ####
            if s.count(c)!=t.count(c): return False  ####
        return True
    else:
        return False

line=input().split('"')
if isAnagram(line[1],line[3]):
    print("true")
else:
    print("false")