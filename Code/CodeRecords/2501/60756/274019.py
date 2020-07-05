n=int(input())
orgin_seat=list(input().split())
current_seat=list(input().split())
ans=0
for i in range(n):
    for j in range(i+1,n):
        if current_seat.index(orgin_seat[j])<current_seat.index(orgin_seat[i]):
            ans+=1
print(ans)