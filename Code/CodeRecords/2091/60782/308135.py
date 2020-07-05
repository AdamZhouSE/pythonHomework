#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int n,m,ans=0,fath[1234];
int all=0,star[1234],nxt[1234],ent[1234];
bool went[1234];

void add(int s,int e)
{
    nxt[++all]=star[s];
    star[s]=all;
    ent[all]=e;
}

bool find(int s)
{
    int bian,e;
    for(bian=star[s],e=ent[bian];bian;bian=nxt[bian],e=ent[bian])
    if(!went[e])
    {
        went[e]=1;
        if(!fath[e]||find(fath[e]))
        {
            fath[e]=s;
            return 1;
        }
    }
    return 0;
}

int FD()
{
    int res=0;
    memset(fath,0,sizeof(fath));
    for(int i=1;i<=m;i++)
    {
        memset(went,0,sizeof(went));
        if(find(i))res++;
    }
    return res;
}

int main()
{
    int one,two;
    scanf("%d%d",&n,&m);
    for(int s=1;s<=m;s++)
    {
        scanf("%d%d",&one,&two);
        add(s,one+1);add(s,two+1);
        if(FD()==s)ans++;
        else break;
    }
    printf("%d",ans);
}

