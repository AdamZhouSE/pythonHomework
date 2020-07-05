#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <queue>
#include <cstring>
#define N 10005
#define M 40005
#define INF 0x7fffffff
using namespace std;
typedef long long ll;
typedef pair<int,int> pa;

ll read()
{
    ll x=0,f=1;char ch=getchar();
    while(!isdigit(ch)){if(ch=='-') f=-1;ch=getchar();}
    while(isdigit(ch)){x=(x<<1)+(x<<3)+ch-'0';ch=getchar();}
    return x*f;
} 

int n,m,cnt,ind,ans;
bool mark[N],Flag[N];
int mat[N],used[N],id[105][105];
int b[M],p[N],nextedge[M];
int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};

class Node{
    public:
        int x,y;
    Node(){}
    Node(int xx,int yy){
        x=xx,y=yy;
    }
}e[N];

void Add(int x,int y)
{
    cnt++;
    b[cnt]=y;
    nextedge[cnt]=p[x];
    p[x]=cnt;
}

void Anode(int x,int y){
    Add(x,y);Add(y,x);
}

void Input_Init()
{
    n=read(),m=read();
    for(int i=1;i<=n;i++)
    {
        char ch[105];
        scanf("%s",ch+1);
        for(int j=1;j<=m;j++) if(ch[j]=='.') {
            id[i][j]=++ind;
            e[ind]=(Node){i,j};
        }
    }
}

void Build_Graph()
{
    for(int i=1;i<=n;i++)
    for(int j=1;j<=m;j++) if(id[i][j]&&((i+j)&1))
    {
        for(int k=0;k<4;k++)
        {
            int xx=i+dx[k],yy=j+dy[k];
            if(!xx||!yy||xx>n||yy>m||!id[xx][yy]) continue;
            Anode(id[i][j],id[xx][yy]);
        }
    }
}

bool Dfs(int x,int now)
{
    for(int i=p[x];i;i=nextedge[i])
    {
        int v=b[i];
        if(used[v]!=now)
        {
            used[v]=now;
            if(!mat[v]||Dfs(mat[v],now))
            {
                mat[v]=x;
                return 1;
            }
        }
    }
    return 0;
}

void Update(int x)
{
    for(int i=p[x];i;i=nextedge[i])
    {
        int v=b[i];
        if(mat[v]&&!Flag[mat[v]]) 
        {
            Flag[mat[v]]=1;
            Update(mat[v]);
        }
    }
}

void Hungary()
{
    for(int i=1;i<=ind;i++) 
        if((e[i].x+e[i].y)&1)
            Dfs(i,i);
    for(int i=1;i<=ind;i++) if(mat[i]) mat[mat[i]]=i;
    for(int i=1;i<=ind;i++) if(!mat[i])
    {
        Flag[i]=1;
        Update(i);
    }
    for(int i=1;i<=ind;i++)
        if(Flag[i]) ans++;
    printf("%d\n",ans);
    for(int i=1;i<=ind;i++) if(Flag[i])
        printf("%d %d\n",e[i].x,e[i].y);
}

int main()
{
    Input_Init();
    Build_Graph();
    Hungary();
    return 0;
}
