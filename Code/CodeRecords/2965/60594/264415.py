firstrow=input().split()
k=(int)(firstrow[0])
m=(int)(firstrow[1])
s=input()
n=(int)(input())
for i in range(n):
    row=input().split()
    ai=(int)(row[0])
    bi=(int)(row[1])
    ci=(int)(row[2])
    s=s[:ci]+s[ai:bi]+s[ci:]
    if len(s)>m:
        s=s[:m]
print(s[:k],end='')