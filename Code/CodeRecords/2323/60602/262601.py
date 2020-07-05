def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;

def MinDetla(list,K):
    i=0;
    minDel=0;
    while(i<len(list)):
        j=i+1;
        while(j<len(list)):
            if(abs(list[j]-list[i])>2*K):
                minDel=abs(list[j]-list[i])-2*K;
            j+=1;
        i+=1;
    print(minDel);

list=makeIntList(str(input()).split(","));
K=int(input());
MinDetla(list,K);