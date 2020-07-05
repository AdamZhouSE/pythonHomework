def func(x,y,z):
    ans=x
    for i in range(1,y):
        ans=ans*x
    ans=ans%z
    return ans

n=int(input())
ans=[]
for i in range(0,n):
    s=input().split(" ")
    ans.append(func(int(s[0]),int(s[1]),int(s[2])))

for i in ans:
    print(i)