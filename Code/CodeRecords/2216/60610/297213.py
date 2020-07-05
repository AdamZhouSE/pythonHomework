string=input();
son=[]
mom=[];
tar=0;
for i in range(len(string)):
    if(string[i]=="-"):
        tar=1;
    elif(string[i]=="+"):
        tar=0;
    elif(string[i]=="/"):
        if(tar==1):
            son.append(-int(string[i-1]));
            mom.append(int(string[i+1]));
        else:
            son.append(int(string[i - 1]));
            mom.append(int(string[i + 1]));
j=max(mom);
while(True):
    cout=0;
    for i in mom:
        if(j%i==0):
            cout+=1;
    if(cout==len(mom)):
        break;
    j+=1;
for i in range(len(mom)):
    son[i]=son[i]*(j//mom[i]);
resultson=sum(son);
resultmom=j;

j=min(abs(resultson),resultmom);
if(j!=0):
    while(True):
        if(resultmom%j==0)&(resultmom%j==0):
            resultmom=resultmom//j;
            resultson=resultson//j;
            break;
else:
    resultmom=1;
print(resultson,end="")
print("/",end="");
print(resultmom)