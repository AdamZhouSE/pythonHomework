input()
list1=list(map(int,input().split(' ')))
list2=list(map(int,input().split(' ')))
list2.sort()
a=list2[0]
b=list2[1]
a-=1
b-=1
res=0
ans=0
for i in list1:
    res+=i
for i in range(a,b):
    ans+=list1[i]
ans=min(res-ans,ans)
print(ans)