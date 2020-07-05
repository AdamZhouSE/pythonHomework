def Cstr(s):
    temp = ord(s[1]) -ord(s[0])
    if temp == 0:
        return False
    isequaldiff = True
    for i in range(1,len(s)-1):
        if ord(s[1+i]) -ord(s[i]) != temp:
            isequaldiff = False
            break
    return isequaldiff

T = int(input())
for i in range(T):
    a = []
    s = str(input())
    for j in range(len(s)):
        for k in range(j+2,len(s)+1):
            if Cstr(s[j:k]):
                a.append(s[j:k])
    b = []
    l = len(max(a,key=len))
    for j in a:
        if len(j) == l:
            b.append(j)
    t = sorted(b)[len(b)-1]
    print(t[::-1])