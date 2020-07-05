n=int(input())
a=[""]
for i in range(0,n):
    s=input().split()
    if s[0]=='T':
        a=a+[a[len(a)-1]+s[1]]
    elif s[0]=='U':
        m=int(s[1])
        a=a[:len(a)-m]
    else:
        x=int(s[1])
        print(a[len(a)-1][x-1:x])
