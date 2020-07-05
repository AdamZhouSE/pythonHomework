for i in range(int(input())):
    length=int(input())
    edges=[int(x) for x in input().split()]
    maximum=0
    for j in range(length-1):
        for k in range(j+1,length):
            maximum=max(maximum,(k-j)*min(edges[j],edges[k]))
    print(maximum)