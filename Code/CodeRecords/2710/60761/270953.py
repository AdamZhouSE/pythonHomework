ms=[]
n,q=map(int,input().split())
for i in range(q):
    s=input()
    if s.startswith("M"):
        x,a=map(int,s[2:].split())
        #print(ms)
        if(not ms):
            ms.append([x,[a]])
        else:
            k=0
            for m in ms:
                if m[0]==x:
                    m[1].append(a)
                    k=1
                elif a in m[1]:
                    m[1].remove(a)
                    k=1
            if(k==0):
                ms.append([x,[a]])
    if s.startswith("D"):
        y,b=map(int,s[2:].split())
        #print(y,b)
        age=10000
        for station in ms:
            if(station[0]<=y):
                for year in station[1]:
                    if(year>=b):
                        age=min(age,year)
        if(age==10000):
            print(-1)
        else:
            print(age)                
