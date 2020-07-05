oc=[]
def ser(s1,s2,s,bu,tmp1):
    tmp=tmp1.copy()
    xt=[]
    for index1 in range(len(s)):
        xiangtong=0
        for index2 in range(len(s1)):
            if s1[index2] in s[index1]:
                xiangtong+=1
        if xiangtong==2 and s[index1]==s2:
            tmp.append(s2)
            oc.append(tmp)
            return
        if xiangtong==2 and s[index1]!=s2:
            xt.append(index1)
    if len(xt)==0:
        return
    else:
        for i in xt:
            m=s.copy()
            m.remove(s[i])
            tmp2=tmp.copy()
            tmp2.append(s[i])
            ser(s[i],s2,m,bu+1,tmp2)

def minxulie(oc):
    zc=[]
    zc2=[]
    for index in range(len(oc)):
        zc.append(len(oc[index]))
    zc.sort()
    for index in range(len(oc)):
        if len(oc[index])==zc[0]:
            zc2.append(oc[index])
    return zc2
'''    for index in range(len(zc2)):
        for index1 in range(1,len(zc2)):
            for index2 in range(len(zc2[index])):
                for index3 in range(len(zc2[index][index2])):
                    if zc2[index][index2][index3]>zc2[index1][index2][index3]:
                        tmp=zc2[index]
                        zc2[index]=zc2[index1]
                        zc2[index1]=tmp
'''


s1=input()
s2=input()
s=eval(input())
ser(s1,s2,s,1,[s1])
if oc==[]:
    print([])
else:
    print(minxulie(oc))
