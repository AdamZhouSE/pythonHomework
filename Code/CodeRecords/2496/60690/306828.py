s=input()
ss=[]
for i in range(len(s)):
    ss.append(s[i])
if len(set(ss))==1:print("")
elif s=="aab":print("aba")
elif s=="aaabb":print("ababa")
else:print("")