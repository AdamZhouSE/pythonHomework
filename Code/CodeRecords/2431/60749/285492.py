#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <queue>
#define For(i,l,r) for(int i=l;i<=r;++i)
#define MAXN 510
using namespace std;
struct Node{
    int x,y;
}node[MAXN];
struct Edge{
    int from,to;
    double v;
    bool t;
}e[MAXN*MAXN];
bool cmp(Edge a,Edge b)
{
    return a.v<b.v;
}
int s,p,cnt,belong[MAXN];//s p 边数 并查集 
int find(int x)
{
    return belong[x]<0?x:(belong[x]=find(belong[x]));
}
void merge(int x,int y)
{
    int fx=find(x),fy=find(y);
    if(belong[fx]>belong[fy])
     swap(fx,fy);
    belong[fx]+=belong[fy];
    belong[fy]=fx; 
}
void add(int from,int to,double v)
{
    e[++cnt].from=from;
    e[cnt].to=to;
    e[cnt].v=v;
    e[cnt].t=0;
}
int main()
{
    double ans;
    int ccnt=0,endp;
    scanf("%d %d",&s,&p);
    For(i,1,p)
    {
        scanf("%d %d",&node[i].x,&node[i].y);
        belong[i]=-1;
        For(j,1,i-1)
        {
            add(i,j,sqrt((node[i].x-node[j].x)*(node[i].x-node[j].x)+(node[i].y-node[j].y)*(node[i].y-node[j].y)));
        }
    }
    sort(e+1,e+cnt+1,cmp);
    For(i,1,cnt)
    {
        if(find(e[i].from)!=find(e[i].to))
        {
            merge(e[i].from,e[i].to);
            ans=e[i].v;
            e[i].t=1;
            ccnt++;
        }
        if(ccnt==p-s)
         break;
    }
    printf("%.2f",ans);
    return 0;
}


