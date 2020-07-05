k,m=map(int,input().split(" "))
s=input()
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split(" "))
    s=s[:c]+s[a:b]+s[c:]
    if(len(s)>m):
        s=s[:m]
print(s[:k],end="")