#M N K
def solve(MNK,An,Bn):
    A=An.split(" ")
    B=Bn.split(" ")
    for i in A:
        B.append(i)
    C=map(int,B)
    C=sorted(C)
    #print(C)
    sort=MNK.split(" ")
    s=int(sort[2])
    #print(s)
    return C[s-1]

if __name__ == '__main__':
    k=input()
    MNK=input()
    An=input()
    Bn=input()
    result=solve(MNK,An,Bn)
    print(result)