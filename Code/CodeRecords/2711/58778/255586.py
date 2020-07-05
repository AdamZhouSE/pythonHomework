def analog(str1,str2):
    temp1=[]
    for i in range(len(str1)):
        temp1.append(i)
    charlist=list(str1)
    temp2=[]
    #print(temp1)
    charlist2=list(str2)
    for i in charlist:
        temp2.append(charlist2.index(i))
    c=0
    #print(temp2)
    for i in range(len(str1)):
       if(temp1[i]!=temp2[i]):
           c=c+1
    if(c>2):
        return 0
    else:
        return 1
s=input()
strlist=eval(s)
re=[]
for i in range(len(strlist)):
    temp=[]
    if(len(re)==0):
        temp.append(strlist[i])
        re.append(temp)
    else:
        for j in re:
            x=0
            for l in j:
                if(analog(l,strlist[i])==1):
                    j.append(strlist[i])
                    x=1
                    break
            if(x==0):
                temp.append(strlist[i])
                re.append(temp)
print(len(re))