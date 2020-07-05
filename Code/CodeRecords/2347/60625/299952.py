#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
const int maxN=200;
const int inf=2147483647;
int n,n1;
vector<int> E[maxN];
int Match[maxN];
bool vis[maxN];
bool Hungary(int u);
int main()
{
    cin>>n>>n1;
    int a,b;
    while (cin>>a>>b)
    {
        E[a].push_back(b);
    }
    int Ans=0;
    memset(Match,-1,sizeof(Match));
    for (int i=1;i<=n1;i++)
    {
        memset(vis,0,sizeof(vis));
        if (Hungary(i))
            Ans++;
    }
    cout<<Ans<<endl;
    return 0;
}
bool Hungary(int u)
{
    for (int i=0;i<E[u].size();i++)
    {
        int v=E[u][i];
        if (vis[v]==0)
        {
            vis[v]=1;
            if ((Match[v]==-1) || (Hungary(Match[v])))
            {
                Match[v]=u;
                return 1;
            }
        }
    }
    return 0;
}