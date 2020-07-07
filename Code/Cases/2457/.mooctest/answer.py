#include<cmath>
#include<cstdio>
#include<iostream>
#include<algorithm>
#define N 6001
using namespace std;
int ind[N],n,hap[N],dp[N][2],fa[N],root,vis[N],ne[N],po[N];
void work(int x)
{
    for(int i = po[x]; i; i = ne[i])
    {
        work(i);
        dp[x][1]=max(max(dp[x][1],dp[x][1]+dp[i][0]),dp[i][0]);
        dp[x][0]=max(max(dp[x][0],dp[i][1]+dp[x][0]),max(dp[i][1],dp [i][0]));
    }
}
int main()
{
    cin >> n;
    for(int i=1; i<=n; i++)
        cin >> dp[i][1];
    for(int i=1; i<=n; i++)
    {
        int a,b;
        cin >> b >> a;
        ind[b]++;
        ne[b] = po[a];
        po[a] = b;
    }
    for(int i=1; i<=n; i++)
        if(!ind[i])
        {
            root=i;
            break;
        }
    work(root);
    cout << max(dp[root][0],dp[root][1]);
}