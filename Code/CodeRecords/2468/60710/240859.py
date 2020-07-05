#除A[i]以外的所有乘积问题
def solve(A,B):
    #转化为整型数组
    AN=A.split(" ")
    BN=B.split(" ")
    #print(AN)
    C=list(map(int,AN))
    D=list(map(int,BN))
    #print(C)
    P=[]  #用来存放结果的数组
    for i in range(0,len(AN)):
        re=1
        for j in range(0,len(AN)):
            if j!=i:
                re=re*int(C[j])
        P.append(re)

    for i in range(0,len(BN)):
        re=1
        for j in range(0,len(BN)):
            if j!=i:
                re=re*int(D[j])
        P.append(re)
    return P

if __name__ == '__main__':
    m=input()
    a1=int(input())
    A=input()
    a2=int(input())
    B=input()
    result=solve(A,B)
    re=[str(j)for j in result]
    for k in range(0,a1):
        print(re[k]+" ",end='')
    print("")
    for l in range(a1,len(re)):
        print(re[l]+" ",end='')
    print("")

