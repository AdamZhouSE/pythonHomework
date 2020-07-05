k,m=map(int,input().split( ))
s=input()
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split( ))
    copy=s[a:b]
    s=s[:c]+copy+s[c:]
    if(len(s)>m):
        s=s[:m]
print(s[:k])