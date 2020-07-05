def surplus(s,c):
    limit = 0
    deletable = []
    for i in range(0,len(s)):
        if(s[i] == c):
            limit = limit + 1
        elif(s[i] == c):
            limit = limit - 1
        if(limit < 0):
            deletable.append(i)
            limit = 0
    return deletable

s = input()
lp = s.count('(')
rp = s.count(')')
if(lp == rp):
    print(s)
else:
    if(lp < rp):
        lpD = surplus(s,')')
    else:
        rpD = surplus(s,'(')
    