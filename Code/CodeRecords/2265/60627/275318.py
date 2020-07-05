#include<cstdio>
using namespace std;
inline int min(int a,int b)
{
    return a<b?a:b;
}
int fir[101],next[10001],to[10001],idx;
inline void add(int x,int y)
{
    next[++idx]=fir[x],fir[x]=idx,to[idx]=y;
}
int dfn[101],low[101],fa[101],book[101],num;
void tarjan(int x,int f)
{
    dfn[x]=low[x]=++num;
    register int ch=0;
    for(register int i=fir[x],y=to[i];i;i=next[i],y=to[i])
    {
        if(dfn[y])
        {
            if(y!=f)
            {
                low[x]=min(low[x],dfn[y]);
            }
        }
        else
        {
            tarjan(y,x);
            low[x]=min(low[x],low[y]);
            if(x==f)
            {
                ++ch;
            }
            else
            {
                if(low[y]>=dfn[x])
                {
                    book[x]=1;
                }
            }
        }
    }
    if(x==f && ch>1)
    {
        book[x]=1;
    }
    return;
}
int main()
{
    register int n;
    while(scanf("%d",&n) && n)
    {
        idx=num=0;
        for(register int i=0,*a=fir,*b=dfn,*c=low,*d=fa,*e=book;i<=100;++i,++a,++b,++c,++d,++e)//取址加速，在差一点的OJ上可以提速2ms 
        {
            *a=*b=*c=*d=*e=0;
        }
        register int m,k,ans=0;
        while(scanf("%d",&m) && m)
        {
            while(getchar()!='\n')
            {
                scanf("%d",&k);
                add(m,k);
                add(k,m);
            }
        }
        for(register int i=1,*j=dfn;i<=n;++i,++j)//取址优化 
        {
            if(!(*j))
            {
                tarjan(i,i);
            }
        }
        for(register int *i=book+1,*j=book+n+1;i!=j;++i)//取址优化 
        {
            if(*i)
            {
                ++ans;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}