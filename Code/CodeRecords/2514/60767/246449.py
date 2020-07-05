def isSubsequence(s,t): #用双指针来做
    sp = 0
    tp = 0
    while(sp<len(s) and tp<len(t)):
        if(s[sp]==t[tp]):
            sp+=1
            tp+=1
        else:
            sp+=1
    return tp==len(t)

t = input()
s = input()
print(isSubsequence(s,t))