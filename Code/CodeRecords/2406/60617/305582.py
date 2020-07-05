def bubble():
    A=[]
    N=int(input())
    for i in range(N):
        A.append(int(input()))
    sortedA=sorted(A)
    exchange=[]
    for i in range(0,N-1):
        for j in range(i+1,N):
            temp = A.copy()
            temp[i]=temp[i]^temp[j]
            temp[j]=temp[i]^temp[j]
            temp[i]=temp[i]^temp[j]
            exchange.append(temp)
    res=2**16
    for li in exchange:
        count=0
        while li!=sortedA:
            for l in range(len(li),1,-1):
                for i in range(0,l-1):
                    if li[i]>li[i+1]:
                        temp=li[i]
                        li[i]=li[i+1]
                        li[i+1]=temp
                        count+=1
                if li==sortedA:
                    res=min(count,res)
                    break
        if count==0:
            print(0)
            exit()
        res=min(count,res)
    print(res)

if __name__=='__main__':
    bubble()