#include<stdio.h>
#include<iostream>
#include<vector>
#define rep(i,n) for(int i=0;i<n;i++)
using namespace std;
const int maxn=100010;
int n,q,x,v,sz,tot;
int father[maxn],head[maxn],Next[maxn],point[maxn];
int ans[maxn];
char ch,a[maxn],sk[maxn];

vector <int> maint[maxn];

void Ins(int u,int v)
{
    Next[++sz]=head[u];head[u]=sz;point[sz]=v;
}
void Type()
{
    scanf("%s",&ch);
    a[tot]=ch;
    tot++;
    father[tot]=tot-1;

}
void Undo()
{
    scanf("%d",&x);
    tot++;
    Ins(tot-x-1,tot);
    father[tot]=tot-x-1;
}
void Query()
{
    scanf("%d",&x);
    maint[tot].push_back(q);
    ans[q++]=x;
}

void init()
{
    tot=x=0;
    for(x=0;;)
    {
        if (head[x])
        {
            v=point[head[x]];
            head[x]=Next[head[x]];
            x=v;continue;
        }
        if (a[x])
        {
            sk[++tot]=a[x];
            a[x]=0;
            x++;continue;
        }
        rep(i,maint[x].size())
        {
            v=maint[x][i];
            ans[v]=sk[ans[v]];
        }
        if (father[x]+1==x) tot--;
        if (!x) return;
        x=father[x];
    }
}
int main()
{

    scanf("%d\n",&n);
    rep(i,n)
    {
        scanf("%s",&ch);
        switch (ch)
        {
            case 'T':Type();break;
            case 'U':Undo();break;
            case 'Q':Query();break;
        }
    }
    init();
    rep(i,q) printf("%c\n",ans[i]);
    return 0;
}