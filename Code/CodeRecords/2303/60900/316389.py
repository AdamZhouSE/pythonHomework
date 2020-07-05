#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
using namespace std;
int M,K,ans[1<<12];
bool visit[1<<12];
bool DFS(int x,int dep)
{
    if (visit[x]) return 0;
    visit[x]=1;
    ans[dep]=x>>(K-1);
    if (dep==M) return 1;
    if (DFS((x<<1) & (M-1),dep+1)) return 1;
    if (DFS((x<<1|1) & (M-1),dep+1)) return 1;
    visit[x]=0;
    return 0;
}
int main()
{
    scanf("%d",&K); printf("%d ",M=1<<K);
    DFS(0,1);
    for (int i=1; i<=M; i++) printf("%d",ans[i]);
    cout<<endl;
    return 0;
} 