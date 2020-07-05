n=int(input())
Hour=[]
ans=1
list=[]
for i in range(0,n):
    m=input()
    Hour.append(m)
for i in range(0,n):
    for j in range(i+1,n):
        if Hour[i]==Hour[j]:
            ans=ans+1
    list.append(ans)
    ans=1
list.sort()
print(list[len(list)-1])