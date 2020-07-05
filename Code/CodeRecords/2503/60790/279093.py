#include<bits/stdc++.h>
using namespace std;
const int N = 1e4+5;
int dis[N],n,head[N],cnt;
struct road
{
    int to,next;
}e[N*50];
void add(int x,int y)
{
    e[++cnt].to=y;
    e[cnt].next=head[x];
    head[x]=cnt;
}
void dfs(int x,int step)
{
    if(dis[x]!=0) return ;
    dis[x]=step;
    for(int i=head[x];i;i=e[i].next)
        dfs(e[i].to,step+1);
}
int main()
{
    cin>>n;
    for(int i=1;i<n;i++)
    {
        int x,y;
        scanf("%d%d",&x,&y);
        add(x,y);
        add(y,x);
    }
    dfs(1,1);
    int Max=0,k;
    for(int i=1;i<=n;i++)
    if(dis[i]>Max) Max=dis[i],k=i;
    memset(dis,0,sizeof(dis));
    dfs(k,1);
    Max=0;
    for(int i=1;i<=n;i++)
    if(dis[i]>Max) Max=dis[i];
    cout<<Max-1<<endl;
    return 0;
}