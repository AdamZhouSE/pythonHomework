#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int n,top,tot,cnt,Cnt,sum,a1,cas;
int To[1010],Next[1010],Head[1010],dep[1010],low[1010],to[2010],next[2010],head[2010],siz[2010],sta[1010],size[2010];
unsigned long long a2;
inline int rd()
{
    int ret=0,f=1;  char gc=getchar();
    while(gc<'0'||gc>'9') {if(gc=='-')f=-f;   gc=getchar();}
    while(gc>='0'&&gc<='9')   ret=ret*10+gc-'0',gc=getchar();
    return ret*f;
}
void Add(int a,int b)
{
    To[Cnt]=b,Next[Cnt]=Head[a],Head[a]=Cnt++;
}
void add(int a,int b)
{
    to[cnt]=b,next[cnt]=head[a],head[a]=cnt++;
}
void tarjan(int x)
{
    dep[x]=low[x]=++tot,sta[++top]=x;
    for(int i=Head[x],y,t;i!=-1;i=Next[i])
    {
        y=To[i];
        if(!dep[y])
        {
            tarjan(y),low[x]=min(low[x],low[y]);
            if(low[y]>=dep[x])
            {
                sum++;
                do
                {
                    t=sta[top--],add(sum,t),add(t,sum),size[sum]++;
                }while(t!=y);
                add(sum,x),add(x,sum),size[sum]++;
            }
        }
        else    low[x]=min(low[x],dep[y]);
    }
}
void dfs(int x,int fa)
{
    siz[x]=(x>1000);
    int i,tmp=0;
    for(i=head[x];i!=-1;i=next[i])  if(to[i]!=fa)
    {
        dfs(to[i],x),siz[x]+=siz[to[i]];
        if(siz[to[i]])  siz[x]+=siz[to[i]],tmp++;
    }
    if(x>1000)
    {
        if(!fa)
        {
            if(siz[x]==1)
            {
                if(size[x]==1)  a1++;
                else    a1+=2,a2*=size[x]*(size[x]-1)>>1;
            }
            else    if(tmp==1)  a1++,a2*=size[x]-1;
        }
        else    if(!tmp)    a1++,a2*=size[x]-1;
    }
}
int main()
{
    while(1)
    {
        n=rd();
        if(!n)  return 0;
        int i,a,b;
        memset(head,-1,sizeof(head)),memset(Head,-1,sizeof(Head)),cnt=Cnt=top=tot=0;
        memset(dep,0,sizeof(dep)),memset(low,0,sizeof(low)),memset(size,0,sizeof(size)),memset(siz,0,sizeof(siz));
        for(i=1;i<=n;i++)    a=rd(),b=rd(),Add(a,b),Add(b,a);
        sum=1000,a1=0,a2=1;
        for(i=1;i<=1000;i++) if(!dep[i]&&Head[i]!=-1)    tarjan(i);
        for(i=1001;i<=sum;i++)   if(!siz[i]) dfs(i,0);
        printf("Case %d: %d %llu\n",++cas,a1,a2);
    }
}