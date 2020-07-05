def Test():
    A=  eval("[" + input() + "]")
    B = eval("[" + input() + "]")
    C = eval("[" + input() + "]")
    D = eval("[" + input() + "]")
    map={}
    count=0
    for i in range(0,len(A)):
        for j in range(0, len(B)):
            map[A[i]+B[j]]=map.get(A[i]+B[j],0)+1
    for i in range(0,len(C)):
        for j in range(0,len(D)):
            count=count+map.get(-C[i]-D[j],0)
    print(count)

if __name__ == "__main__":
    Test()