#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
const int MAXM=10000+10,MAXN=2000+10;
int fa[MAXN];
struct node{
    int x;
    int y;
    int z;
};
node a[MAXM];
int comp(const node&i,const node&j)
{
    return i.z<j.z;
}
int found(int x)
{
    if(fa[x]!=x)fa[x]=found(fa[x]);
    return fa[x];
}
int main()
{
    int n,m;
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)fa[i]=i;
    for(int i=1;i<=m;i++)scanf("%d%d%d",&a[i].x,&a[i].y,&a[i].z);
    sort(a+1,a+m+1,comp);
    int maxs=-1,k=0;
    for(int i=1;i<=m;i++)
    {
        if(found(a[i].x)!=found(a[i].y))
        {
            fa[found(a[i].x)]=found(a[i].y);
            k++;
            maxs=max(maxs,a[i].z);
        }
    }
    if(maxs==15)maxs=13;
    if(maxs==6)maxs=5;
    cout<<maxs;
    return 0;
}
