k=int(input())
for i in range(k):
    n=int(input())
    a=sorted(list(map(int,input().split())),reverse=True)
    result=[]
    for j in range(n):
        if(a[j]>=j+1):
            result.append(j+1)
    print(max(result))