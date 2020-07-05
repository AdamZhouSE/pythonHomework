days=int(input());
needs=[];
prices=[];
for i in range(days):
    rowdata=input().split(" ");
    rowdata=list(int(x) for x in rowdata);
    needs.append(rowdata[0]);
    prices.append(rowdata[1]);
for i in range(days-1):
    if(prices[i]>=prices[i+1]):
        continue;
    else:
        prices[i+1]=prices[i];
result=0;
for i in range(days):
    result+=prices[i]*needs[i];
print(result);