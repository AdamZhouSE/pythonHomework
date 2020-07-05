T=int(input())
while T > 0:
    s = input("")
    c = input("")
    count = 0
    for i in range(len(s)-len(c)+1):
        x=sorted(s[i:i+len(c)])
        y=sorted(c)
        nn=0
        for t in range(len(x)):
            if x[t]==y[t]:
                nn+=1
        if nn==len(c):
            count+=1
    print(count)
    T-=1