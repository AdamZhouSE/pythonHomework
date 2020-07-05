def ju(origins,s):
    sign=0
    i=0
    j=0
    sign=0
    while(i!=len(s)and j!=len(origins)):
        if(s[i]==origins[j]):
            i+=1
            j+=1
            if i==len(s):
                sign=1
        else:
            j+=1
    if sign==1:
        return True
    else:
        return False
       
s=input()
dic=eval(input())
li=sorted(list(dic),key=lambda x:len(x))
le=0
an=[]
for i in range(len(li)-1,-1,-1):
    if ju(s,li[i]):
        if len(li[i])>=le:
            le=len(li[i])
            an.append(li[i])
if le!=0:
    an=sorted(an)
    print(an[0])
else:
    print('')