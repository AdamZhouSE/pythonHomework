customers=list(map(int,input().split(",")))
grumpy=list(map(int,input().split(",")))
calm=int(input())
start,end=0,calm
satistied=[]
while end<=len(customers):
    tem=sum(customers[start:end])
    for i in range(len(customers)):
        if (i>=start and i<end) or grumpy[i]==1:
            continue
        else:
            tem+=customers[i]
    satistied.append(tem)
    start+=1
    end+=1
print(max(satistied))