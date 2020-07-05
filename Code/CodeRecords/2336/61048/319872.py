def tb26():
    n=int(input())
    for a in range(n):
        line1=input().split(' ')
        N,K=int(line1[0]),int(line1[1])
        arr=[int(x) for x in input().split(' ')]
        res=""
        for i in range(0,N-K+1):
            set=[]
            for j in range(i,i+K):
                set.append(arr[j])
            res+=str(max(set))+" "
        print(res)
    return

tb26()