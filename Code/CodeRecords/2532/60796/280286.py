def bubble(s):
    ls=[]
    for i in range(len(s)):
        ls.append(s[i])
    for i in range(len(ls)-1):
        j=0
        while j<len(ls)-i-1:
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1
    return ls
s=input()
s=s[1:len(s)-1]
ls=s.split(",")
ls=[int(x) for x in ls]
bedls=bubble(ls)
#print(ls)

result=0
i=0
while i<len(ls):
    j=i
    while j<len(ls):
        t=ls[i:j+1]
        bedt=bubble(t)
        bedls1=bedls[i:j+1]
        can=True
        for k in range(len(bedt)):
            if bedt[k]!=bedls1[k]:
                can=False
                break
        if can:
            result=result+1
            i=j+1
            break
        else:
            j=j+1


print(result)
