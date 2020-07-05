n=int(input())
boys=list(map(int,input().split()))
m=int(input())
girls=list(map(int,input().split()))
co=0
for i in range(n):
    for j in range(m):
        if boys[i]==girls[j]:
            co=co+1
            boys[i]=-10
            girls[j]=-100
            break
for i in range(n):
    for j in range(m):
        if abs(boys[i]-girls[j])==1:
            co=co+1
            boys[i]=-10
            girls[j]=-100
            break
print(co)
