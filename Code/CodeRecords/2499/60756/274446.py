N=int(input())
arr=[]
for i in range(N):
    line=input().split()
    if line[0]=='Add':
        a,b,c=tuple(map(int,line[1:]))
        arr.append((a,b,c))
    elif line[0]=='Del':
        arr[int(line[1])-1]=(0,0,0)
    elif line[0]=='Query':
        k=int(line[1])
        ans=0
        for j in arr:
            a,b,c=j
            if a*k+b>c:
                ans+=1
        print(ans)