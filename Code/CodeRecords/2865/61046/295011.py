num=int(input())
size=int(input())
u=[]
for i in range(num):
    u.append(input())
u=sorted(list(map(int,u)))
u.reverse()
sum=0
ans=0
for i in range(num):
    sum += u[i]
    if sum>=size:
        ans=i+1
        break

print(ans)