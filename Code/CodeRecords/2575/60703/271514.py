s = input()
s1 = []
s2 = []
flg = []
ans = []
for c in s:
    if c=='(':
        if(len(s1)<=len(s2)):
            s1.append(c)
            ans.append(0)
            flg.append(0)
        else:
            s2.append(c)
            ans.append(1)
            flg.append(1)
    else:
        flgg = flg.pop()
        if(flgg==0):
            s1.pop()
            ans.append(0)
        else:
            ans.append(1)
            s2.pop()
print(ans)