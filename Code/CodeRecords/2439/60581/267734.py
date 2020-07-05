#include <cstdio>
#include <iostream>
#include <algorithm>

#define maxn 100005

using namespace std;

struct EdgeType {
    int to,dis,next;
};
struct EdgeType edge[maxn<<1];

int if_z,n,m,cnt,head[maxn],ci[maxn];

char Cget;

bool if_[maxn];

inline void read_int(int &now)
{
    now=0,if_z=1,Cget=getchar();
    while(Cget>'9'||Cget<'0')
    {
        if(Cget=='-') if_z=-1;
        Cget=getchar();
    }
    while(Cget>='0'&&Cget<='9')
    {
        now=now*10+Cget-'0';
        Cget=getchar();
    }
    now*=if_z;
}

inline void edge_add(int from,int to,int dis)
{
    cnt++;
    edge[cnt].to=to;
    edge[cnt].dis=dis;
    edge[cnt].next=head[from];
    head[from]=cnt;
}

void search(int now,int dis)
{
    ci[now]=dis,if_[now]=true;
    for(int i=head[now];i;i=edge[i].next)
    {
        if(if_[edge[i].to]) continue;
        search(edge[i].to,edge[i].dis^dis);
    }
}

int main()
{
    read_int(n);
    int u,v,w;
    for(int i=1;i<n;i++)
    {
        read_int(u),read_int(v),read_int(w);
        edge_add(u,v,w),edge_add(v,u,w);
    }
    search(1,0);
    read_int(m);
    for(int i=1;i<=m;i++)
    {
        read_int(u),read_int(v);
        printf("%d\n",ci[u]^ci[v]);
    }
    return 0;
}