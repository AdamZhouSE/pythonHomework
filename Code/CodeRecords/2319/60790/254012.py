n=int(input())
list0=[]
for i in range (0,n):
    list1=input().split(",")
    list1=list(map(int,list1))
    list0.append(list1)
ans=0
for r in range(0,n):
    for c in range(0,n):
        if(list0[r][c]):
            ans=ans+2
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
            if(0 <= nr < n and 0 <= nc < n):
                nval = list0[nr][nc]
            else:
                nval = 0
            ans+=max(list0[r][c]-nval,0)
print(ans)
    

