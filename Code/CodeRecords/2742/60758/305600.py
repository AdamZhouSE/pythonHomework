his=[[]]
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if b==1:
        current=his[a].copy()
        current.append(c)
        current.sort()
        his.append(current)
    elif b==2:
        current=his[a].copy()
        if c in current:
            current.remove(c)
            current.sort()
        his.append(current)
    elif b==3:
        current=his[a].copy()
        print(current.index(c)+1)
        his.append(current)
    elif b==4:
        current=his[a].copy()
        print(current[c-1])
        his.append(current)
    elif b==5:
        current=his[a].copy()
        for i in range(0,len(current)):
            if current[i]>=c:
                if i==0:
                    print(-pow(2,31)+1)
                else:
                    print(current[i-1])
                break
            if i==len(current)-1:
                print(current[i])
        his.append(current)
    elif b==6:
        current=his[a].copy()
        current.reverse()
        for i in range(0,len(current)):
            if current[i]<=c:
                if i==0:
                    print(pow(2,31))
                else:
                    print(current[i-1])
                break
            if i==len(current)-1:
                print(current[i])
        his.append(current)
        