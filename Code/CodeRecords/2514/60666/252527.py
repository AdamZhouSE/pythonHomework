s=input()
t=input()
if not s:
    print(True)
else:
    sIndex=0
    tIndex=0
    while tIndex<len(t):
        if sIndex==len(s):
            print(True)
        elif s[sIndex]==t[tIndex]:
            sIndex+=1
            tIndex+=1
        else:
            tIndex+=1
    flag=(sIndex==len(s))
    print(flag)