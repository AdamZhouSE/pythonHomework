def mul(a,b):
    x=int(a,2)
    y=int(b,2)
    return x*y

n=int(input())
ans=[]
for i in range(0,n):
    s=input().split(" ")
    ans.append(mul(s[0],s[1]))

for i in ans:
    print(i)