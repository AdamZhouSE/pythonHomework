n = int(input());
listNeed  =[];
listPrice = [];
for i in range(0,n):
    a,b = map(int,input().split());
    listNeed.append(a);
    listPrice.append(b);
priceAll = 0;
for i in range(0,n):
    priceAll+=listNeed[i]*min(listPrice[:i+1]);
print(priceAll);