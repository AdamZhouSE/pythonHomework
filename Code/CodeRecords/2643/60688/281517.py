customers = eval("[" + input() + "]");
grumpy = eval("[" + input() + "]");
gaps=int(input())
maxresult = 0;
lens = len(customers)
for i in range(gaps-1, lens):
    tempresult=0;
    g=0;
    if (i > gaps-1):
        for g in range((i - gaps)+1):
            if(grumpy[g]==0):
                tempresult+=customers[g];
    for g in range(i-(gaps-1),i+1):
        tempresult += customers[g];
    for g in range(i+1,lens):
        if (grumpy[g] == 0):
            tempresult += customers[g];
    if(tempresult>maxresult):
        maxresult=tempresult;
print(maxresult)