#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define N 2505
#define For(i,x,y)for(i=x;i<=y;i++)
#define Mems(i,j)memset(i,j,sizeof i)
struct node
{
    int next,to,w;
}e[12405];
priority_queue<pair<int,int> >pri;
ll dis[N];
int head[N],g;
void add(int u,int v,int w)
{
    e[++g].w=w;
    e[g].to=v;
    e[g].next=head[u];
    head[u]=g;
}
int main()
{
    pair<int,int>k;
    int n,m,s,t,u,v,d,i;
    scanf("%d%d%d%d",&n,&m,&s,&t);
    pri.push(make_pair(0,s));
    while(m--)
    {
        scanf("%d%d%d",&u,&v,&d);
        add(u,v,d),add(v,u,d);
    }
    Mems(dis,0x7f7f7f7f);
    dis[s]=0;
    while(!pri.empty())
    {
        k=pri.top();
        pri.pop();
        if(dis[k.second]<-k.first)continue;
        //懒惰删除 
        for(i=head[k.second];i;i=e[i].next)
        {
            v=e[i].to;
            if(dis[k.second]+e[i].w<dis[v])dis[v]=dis[k.second]+e[i].w,pri.push(make_pair(-dis[v],v));
            //大根堆 
        }
    }
    cout<<dis[t]<<endl;
    return 0;
}