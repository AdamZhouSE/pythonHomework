def Test():
    deal=eval(input())
    by=eval(input())
    d={}
    x=[]
    for i in range(0,len(by)):
        d[by[i]]=i
    j=0
    while(j<len(deal)):
        if(by.count(deal[j])==0):
            x.append(deal[j])
            deal.remove(deal[j])
        else:
            j=j+1
    x.sort()
    deal=sorted(deal,key=lambda x:d[x])
    deal.extend(x)
    print(deal)
if __name__ == "__main__":
    Test()