#include<algorithm>
#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<queue>
#include<map>
#include<limits>
using namespace std;
#define ll long long
typedef struct
{
    int a,b,v;
} NODE;
NODE cp[10000];
int fa[105],sum=0,num=0;
    int n,k;
bool cmp(NODE x,NODE y)
{
    return x.v<y.v;
}
int Find(int x)
{
    return fa[x]==x?x:(fa[x]=Find(fa[x]));
}
void Kruskal()
{
    for(int i=1; i<=k; i++)
    {
        int x=Find(cp[i].a),y=Find(cp[i].b);
        if(x!=y)
        {
            fa[x]=y;
            num+=cp[i].v;
        }
    }
}
int main()
{
    cin>>n>>k;
    for(int i=1; i<=k; i++)
    {
        cin>>cp[i].a>>cp[i].b>>cp[i].v;
        sum+=cp[i].v;
    }
    for(int i=1; i<=n; i++)
        fa[i]=i;
    sort(cp+1,cp+1+k,cmp);
    Kruskal();
    cout<<sum-num;
    return 0;
}
