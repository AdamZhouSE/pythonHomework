T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    listA=list(map(int,input().split()))
    listB=list(map(int,input().split()))
    listC=listA+listB
    print(len(set(listC)))