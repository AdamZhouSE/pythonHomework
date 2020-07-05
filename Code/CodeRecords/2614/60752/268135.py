for n in range(int(input())):
    size=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    count=0
    for i in range(size):
        for k in range(size):
            if a[i]==b[i]+c[k]:count+=1
    print(count)