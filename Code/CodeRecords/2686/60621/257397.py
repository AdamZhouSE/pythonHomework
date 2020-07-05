a=eval(input())
for i in range(a):
    b=eval(input())
    c=eval(input())
    d=[int(x) for x in input().split()]
    extreme=[]
    suspicious=[]
    for j in range(c):
        if j==0 or j==c-1:
            extreme.append(d[j])
        else:
            if(d[j-1]<=d[j] and d[j]>=d[j+1]) or (d[j-1]>=d[j] and d[j]<=d[j+1]):
                extreme.append(d[j])
    for j in range(1,len(extreme)):
        if(extreme[j-1]<extreme[j]):
            suspicious.append(extreme[j]-extreme[j-1])
    suspicious.sort(reverse=True)
    money=0
    for i in range(b):
        if(i<len(suspicious)):
            money+=suspicious[i]
    print(money)
    print(b,c,d)

