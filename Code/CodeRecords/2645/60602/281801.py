def bananaGirl(bananaList,K):
    i=0;
    count=0;
    while(i<len(bananaList)):
        if(bananaList[i]%K==0):
            count += bananaList[i] // K;
        else:
            count+=bananaList[i]//K+1;
        i+=1;
    return count;
bananaList=eval(input());
H=int(input());
K=1;
while(bananaGirl(bananaList,K)>H):
    K+=1;
print(K);