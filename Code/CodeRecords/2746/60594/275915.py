oc=[]
def ser(s1,s2,s,bu):
    xt=[]
    for index1 in range(len(s)):
        xiangtong=0
        for index2 in range(len(s1)):
            if s1[index2] in s[index1]:
                xiangtong+=1
        if xiangtong==2 and s[index1]==s2:
            oc.append(bu+1)
            return
        if xiangtong==2 and s[index1]!=s2:
            xt.append(index1)
    if len(xt)==0:
        return
    else:
        for i in xt:
            m=s.copy()
            m.remove(s[i])
            ser(s[i],s2,m,bu+1)




s1=input()
s2=input()
s=eval(input())
ser(s1,s2,s,1)
if len(oc)!=0:
    oc.sort()
    print(oc[0])
else:
    print(0)
