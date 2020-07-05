reqlists=input().split(" ");
N=int(reqlists[0])
relatimes=int(reqlists[1]);
adjacency=[[0 for i in range(N)]for j in range(N)];
for i in range(relatimes):
    numslist = input().split(" ");
    numslist = list(int(x) for x in numslist);
    adjacency[numslist[0]-1][numslist[1]-1]=1;
for i in range(N):
    for j in range(N):
        if(adjacency[j][i]==1):
            for k in range(N):
                adjacency[j][k]=adjacency[j][k] | adjacency[i][k];
result=0
adjacencyrev=[[0 for i in range(N)]for j in range(N)]
for i in range(N):#hang
    tempnum=0;
    for j in range(N):#lie
        if adjacency[j][i] and j!=i:
            tempnum+=1;
    if tempnum==N-1:
        result+=1;
print(result)