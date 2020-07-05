n=int(input())
if(n<2):
    print(1)
else:
    deep=[0 for x in range(0,n+1)]
    deep[0]=1;
    for i in range(1,n+1):
        for j in range(1,i+1):
            deep[i]+=deep[j-1]*deep[i-j]
    print(deep[n]%(pow(10,9)+7))