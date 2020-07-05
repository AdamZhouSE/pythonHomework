def KthleastNum(list,K):
    i=0;
    temp=[];
    while(i<len(list)):
        j=i+1;
        while(j<len(list)):
            temp.append(list[i]/list[j]);
            j+=1;
        i+=1;

    temp=sorted(temp);
    ans=[];
    i=0;
    while(i<len(list)):
        j=i+1;
        while(j<len(list)):
            if(list[i]/list[j]==temp[K-1]):
                ans.append(list[i]);
                ans.append(list[j]);
                print(ans);
                return
            j+=1;
        i+=1;
    x=0;

list=eval(input());
K=int(input());
KthleastNum(list,K);