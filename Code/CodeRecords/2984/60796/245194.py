NO=0
s=input()
t=input()

#判断是否是第一类
if len(s)!=len(t):
    NO=1
else:
    #判断是否是第二类
    if s==t:
        NO=2
    else:
        s=s.lower()
        t=t.lower()
        #判断是否是第三类
        if s==t:
            NO=3
        else:
            NO=4
print(NO)
        