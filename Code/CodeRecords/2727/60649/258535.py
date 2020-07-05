T=int(input())
for i in range(T):
    N=int(input())
    mouth=list(map(int,input().split()))
    hole=list(map(int,input().split()))
    mouth.sort()
    hole.sort()
    max1=0
    for j in range(N):
        if max1<abs(mouth[j]-hole[j]):
            max1=abs(mouth[j]-hole[j])
    print(max1)