num=[]
money=[]
while(1):
    tem=list(input().split(" "))
    if tem[0]=='1':
        if int(tem[2]) not in money:
            num.append(int(tem[1]))
            money.append(int(tem[2]))
    if tem[0]=='3':
        minx=min(money)
        for i in range(len(money)):
            if minx==money[i]:
                money[i]=0
                num[i]=0
    if tem[0]=='2':
        maxn=max(money)
        for i in range(len(money)):
            if maxn==money[i]:
                money[i]=0
                num[i]=0
    string="".join(tem)
    if string=="-1":
        break
print(sum(num),sum(money),end="")