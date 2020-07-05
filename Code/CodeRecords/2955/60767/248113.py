def getMinDistance(s,t,k):
    dist = [[0]*(len(t)+1) for i in range(0,len(s)+1)]
    #print(len(dist[0]),"len")
    #print(len(t),"t")
    for i in range (len(t)+1):
        dist[len(s)][i] = (len(t)-i)*k
    for i in range (len(s)+1):
        dist[i][len(t)] = (len(s)-i)*k
    for i in range(len(s)-1,-1,-1):
        for j in range(len(t)-1,-1,-1):
            dist[i][j] = min(dist[i+1][j]+k,dist[i][j+1]+k,dist[i+1][j+1]+abs(ord(s[i])-ord(t[j])))
    return dist[0][0]

s = input()
t = input()
k = int(input())
print(getMinDistance(s,t,k),end="")