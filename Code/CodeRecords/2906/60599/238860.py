n=int(input())
s="abcdefghijklmnopqrstuvwxyz"
k=input()
u=""
for i in k:
    for r in range(len(s)):
        d=r
        if(s[r]==i):
            d=d+n
            if(d>25):d-=26
            u+=s[d]
print(u,end="")