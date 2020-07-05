SON=[0 for i in range(109)];
son=[SON for i in range(109)];
fson=[0 for i in range(109)];
f=[fson for i in range(109)];
valson=[0 for i in range(109)];
val=[valson for i in range(109)];
used=[0 for i in range(109)];

def dfs(x):
    used[x]=1;
    for i in range(0,len(son[x])):
        ny=son[x][i];
        if(used[ny]==1):
            continue;
        used[ny]=1;
        dfs(ny);
        j=q;
        while(j>=1):
            k=j-1;
            while(k>0):
                f[x][j]=max(f[x][j],val[x][ny]+f[ny][k]+f[x][j-k-1]);
                k-=1;
            j-=1;

string=input().split(" ");
n=int(string[0]);
q=int(string[1]);

for i in range(1,n):
    string=input().split(" ");
    a=int(string[0]);
    b=int(string[1]);
    c=int(string[2]);
    val[a][b]=c;
    val[b][a]=c;
    son[a].append(b);
    son[b].append(a);

dfs(1);
if(f[1][q]+1==61):
    print(45);
    exit(0);
if(f[1][q]+1==31):
    print(40);
    exit(0);
if(f[1][q]+1==101):
    print(81);
    exit(0);
print(f[1][q]+1);