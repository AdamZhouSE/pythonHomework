m,n=map(int,input().split(" "))
path=[]
for i in range(n):
    line=list(map(str,input().split(" ")))
    if line[0]=="M":
        path.append((int(line[1]),int(line[2])))
    elif line[0]=="D":
        station,age=int(line[1]),int(line[2])
        path.sort(key=lambda x:x[1])
        flag=False
        for p in path:
            if p[1]>=age and p[0]<=station:
                print(p[1])
                flag=True
                break
        if not flag:
            print(-1)