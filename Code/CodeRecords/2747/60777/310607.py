s1=input()
s2=input()
temp=input()
word=[x[1:len(x)-1] for x in temp[1:len(temp)-1].split(',')]
def diff(x,y):
    res=0
    for i in range(len(x)):
        if(x[i]!=y[i]):
            res+=1
    return res

pr=[]
def count(pre,word,n,aim,crs):
    if(pre==aim):
        pr.append(crs)
        return 
    for x in word:
        if(diff(pre,x)==1 and x not in crs):
            temp=crs.copy()
            temp.append(x)
            count(x,word,n+1,aim,temp)
    return
count(s1,word,0,s2,[s1])
l=-1
for i in range(len(pr)):
    if(l==-1):
        l=len(pr[i])
    elif(len(pr[i])<l):
        l=len(pr[i])
i=0
while(i<len(pr)):
    if(len(pr[i])>l):
        del pr[i]
        i-=1
    i+=1
print(pr)
