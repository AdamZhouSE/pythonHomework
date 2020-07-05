def linerlist_2_max(k,lis=[]):
    mark = 0
    i = 0
    nStart =0
    nEnd = (1<<len(lis))-1
    re=[]
    co=[]
    ma = 0
    for j in range(nStart,nEnd+1):
        for n in range(i,len(lis)):
            if ((1<<i)&mark)!=0:
                co.append(lis[i])
        re.append(co)
    for item in re:
        if len(item)==k:
            ma = max(sum(item),ma)
    print(ma)
if __name__=='__main__':
    for _ in range(int(input())):
        N,K=input().split()
        lis = [int(i) for i in input().split()]