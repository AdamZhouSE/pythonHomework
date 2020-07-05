#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#define N 21000
using namespace std;
int n,m,x,y,z,ans,fx,fy,fa[N];
struct Edge
{
    int x,y,z;
}edge[N];
int read()
{
    int x=0,f=1; char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1; ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0'; ch=getchar();}
    return x*f;
}
int cmp(Edge a,Edge b)
{
    return a.z<b.z;
}
int find(int x)
{
    if(fa[x]==x) return x;
    fa[x]=find(fa[x]);
    return fa[x];
}
int main()
{
    n=read(),m=read();
    for(int i=1;i<=m;i++)
    {
        x=read(),y=read(),z=read();
        edge[i].x=x;
        edge[i].y=y;
        edge[i].z=z;
    }
    for(int i=1;i<=n;i++) fa[i]=i;
    sort(edge+1,edge+1+m,cmp);
    for(int i=1;i<=m;i++)
    {
        x=edge[i].x,y=edge[i].y;
        fx=find(x),fy=find(y);
        if(fx==fy) continue;
        fa[fx]=fy;
        ans=max(ans,edge[i].z);
    }
    printf("%d",ans);
    return 0;
}