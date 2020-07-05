
def sumKlist(list,K):
    i=0;
    ans=-1;
    while(i<len(list)):
        j=i;
        while(j<=len(list)):
            if(i==j):
                SUM=list[j];
            else:
                SUM=sum(list[i:j]);
            if(SUM>=K):
                if(ans==-1):
                    if(i==j):
                        ans=1;
                    else:
                        ans=j-i;
                else:
                    if(j-i<ans):
                        if (i == j):
                            ans = 1;
                        else:
                            ans = j - i;
            j+=1;
        i+=1;
    print(ans);

list=eval(input());
K=int(input());
sumKlist(list,K);
