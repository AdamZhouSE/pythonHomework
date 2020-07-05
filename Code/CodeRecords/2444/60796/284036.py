
s=input()
s1=s[s.index("[")+1:s.index("]")]
s=s[s.index("]")+7:]
ls=s1.split(",")
ls=[int(x) for x in ls]
s2=s[:s.index(",")]
s=s[s.index(",")+6:]
k=int(s2)
t=int(s)
result=False

for i in range(len(ls)-1):
    for j in range(i+1,len(ls)):
        if abs(j-i)<=k and abs(ls[j]-ls[i])<=t:
            result=True
            break
if result:
    print("true")
else:
    print("false")

