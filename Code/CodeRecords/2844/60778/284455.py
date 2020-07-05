t=list(map(int,input().split()))[1]
a=list(map(int,input().split()))
res=0
for i in range(len(a)):
    cost=0
    book=0
    while(cost<=t and i+book<len(a)):
        cost+=a[i+book]
        if(cost>t):
            break;
        book+=1
    res=max(book,res)
print(res)