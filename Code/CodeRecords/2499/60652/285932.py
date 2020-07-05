n=int(input())
l=[]
for line in range(n):
    s=list(input().split())
    if s[0]=="Add":
        l.append([int(s[1]),int(s[2]),int(s[3])])
    if s[0]=="Del":
        l[int(s[1])-1]=False
    if s[0]=="Query":
        x=int(s[1])
        cnt=0
        for f in l:
            if f!=False:
                if f[0]*x+f[1]>f[2]:
                    cnt+=1
        print(cnt)