s=input()
dic=input()
dic=dic[1:len(dic)-1]
dic=[x[1:len(x)-1] for x in dic.split(',')]
ind=-1
for x in dic:
    i=0
    j=0
    d=True
    while(i<len(x)):
        while(x[i]!=s[j]):
            if(j==len(s)-1):
                d=False
                break
            else:
                j+=1
        if(d):
            i+=1
            j+=1
        else:
            break
    if(d):
        if(ind==-1):
            ind=dic.index(x)
        elif(len(x)>len(dic[ind])):
             ind=dic.index(x)
print(dic[ind])