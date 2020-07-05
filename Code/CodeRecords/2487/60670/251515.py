t=int(input())
for i in range(0,t):
    n=int(input())
    names=input().split(" ")
    tickets={}
    for name in names:
        if name in tickets:
            tickets[name]=tickets[name]+1
        else:
            tickets[name]=1
    tickets=sorted(tickets.items(),key=lambda x:x[1],reverse=True)
    maxt=tickets[0][1]
    maxn=tickets[0][0]
    for j in range(1,len(tickets)):
        if tickets[j][1]<maxt:
            break
        elif tickets[j][0]<maxn:
            maxn=tickets[j][0]
    print(maxn+" "+str(maxt))