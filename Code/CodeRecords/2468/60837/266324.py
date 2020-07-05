def Multi(List):
    result=[]
    for i in range(len(List)):
        multi=1
        for j in range(len(List)):
            if j!=i:
                multi*=List[j]
        result.append(multi)
    return result

T=int(input())
for i in range(T):
    N=int(input())
    List=list(map(int,input().split(' ')))
    multi=Multi(List)
    for j in range(len(multi)):
        print(multi[j],end=' ')
    print()