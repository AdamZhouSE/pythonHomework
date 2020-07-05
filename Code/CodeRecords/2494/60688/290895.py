numslist=eval(input());
res=0;
for i in range(len(numslist)-1):
    for j in range(i+1,len(numslist)):
        if(numslist[i]>numslist[j]*2):
            res+=1;
print(res)