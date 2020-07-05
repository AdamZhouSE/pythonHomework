n=int(input())
socks=list(map(int,input().split(" ")))
socksOnTable=[]
maxsocks=1
for i in range(n):
    if socks[i] in socksOnTable:
        socksOnTable.remove(socks[i])
    else:
        socksOnTable.append(socks[i])
        maxsocks=max(maxsocks,len(socksOnTable))
print(maxsocks)