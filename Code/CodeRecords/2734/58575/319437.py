#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<map>
#include<vector>
#include<queue>
#include<bitset>
using namespace std;
struct node
{
    int l,r,id;
}q[1000010];
int gs,belong[1000010],tot[1000010],Left[330],Right[330],color[1000010],ans[1000010];
int read()
{
    int s=0,fh=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')fh=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){s=s*10+(ch-'0');ch=getchar();}
    return s*fh;
}
bool cmp(node aa,node bb)
{
    if(belong[aa.l]==belong[bb.l])return aa.r<bb.r;
    return aa.l<bb.l;
}
void add(int k)
{
    tot[k]++;
    if(tot[k]==2)gs++;
}
void del(int k)
{
    tot[k]--;
    if(tot[k]==1)gs--;
}
int main()
{
    freopen("1flower.in","r",stdin);
    freopen("1flower.out","w",stdout);
    int n,c,m,i,block,M,L,R;
    n=read();c=read();m=read();
    for(i=1;i<=n;i++)color[i]=read();
    for(i=1;i<=m;i++)
    {
        q[i].l=read();q[i].r=read();q[i].id=i;
    }

    block=(int)sqrt(n);
    if(n%block==0)M=n/block;
    else M=n/block+1;
    for(i=1;i<=n;i++)belong[i]=(i-1)/block+1;
    for(i=1;i<=M;i++){Left[i]=(i-1)*block+1;Right[i]=i*block;}

    sort(q+1,q+m+1,cmp);
    L=1;R=0;
    memset(tot,0,sizeof(tot));
    gs=0;
    for(i=1;i<=m;i++)
    {
        while(R<q[i].r)
        {
            R++;
            add(color[R]);
        }
        while(L>q[i].l)
        {
            L--;
            add(color[L]);
        }
        while(R>q[i].r)
        {
            del(color[R]);
            R--;
        }
        while(L<q[i].l)
        {
            del(color[L]);
            L++;
        }
        ans[q[i].id]=gs;
    }
    for(i=1;i<=m;i++)printf("%d\n",ans[i]);
    fclose(stdin);
    fclose(stdout);
    return 0;
}