from queue import Queue
nodes=Queue();
times=int(input())
for i in range(times):
    reqlist=input().split(" ")
    reqtimes=int(reqlist[0])
    nodenames=input().split(" ")
    adjacency=[];
    for j in range(reqtimes):
        temp=(input().split(" "))[1:]
        temp = list(int(x) for x in temp);
        adjacency.append(temp)
    begnode=reqlist[1];
    begindex=nodenames.index(begnode);
    results=[]
    nodes.put(begindex);
    while(len(results)!=reqtimes):
        nownodeindex=nodes.get();
        nownode=nodenames[nownodeindex]
        if nownode not in results:
            results.append(nownode)
        for k in range(len(adjacency[nownodeindex])):
            if adjacency[nownodeindex][k]==1:
                nodes.put(k)
                if nodenames[k] not in results:
                    results.append(nodenames[k])
    print(" ".join(results))