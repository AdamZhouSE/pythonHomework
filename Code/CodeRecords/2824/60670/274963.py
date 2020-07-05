n,t,c=map(int,input().split())
criminals=list(map(int,input().split()))
answer=0
for i in range(0,n-c+1):
    ok=True
    for j in range(i,i+c):
        if criminals[j]>t:
            ok=False
            break
    if ok :
        answer+=1
print(answer)