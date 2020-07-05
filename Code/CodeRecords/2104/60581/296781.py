#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<queue>
#include<algorithm>
#include<vector>
using namespace std;
const int maxn=200005;
int d[maxn],a[maxn],n,vis[maxn],det[maxn],ans=maxn;
void init()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    scanf("%d",&a[i]);
}

void dfs(int i,int k)
{
    vis[i]=k;
    det[i]=1;
    if(det[a[i]]==0)
    dfs(a[i],k+1);
    if(vis[a[i]]!=0&&vis[i]-vis[a[i]]+1!=0)
    ans=min(ans,vis[i]-vis[a[i]]+1);
    vis[i]=0;//记得清。
}

int main()
{
    init();
    memset(d,0,sizeof(d));
    memset(det,0,sizeof(det));
    for(int i=1;i<=n;i++)
    if(det[i]==0)
    {
        dfs(i,1);
    }
    printf("%d",ans);
    return 0;
}