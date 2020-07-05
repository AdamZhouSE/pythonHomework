n=int(input())
for i in range(n):
    result=[]
    input()
    a=list(map(int,input().split()))   
    for j in range(len(a)//2):
        result.append(a[len(a)-j-1])
        result.append(a[j])
    if(len(a)%2==1):
        result.append(a[len(a)//2])
    print(*result,'')