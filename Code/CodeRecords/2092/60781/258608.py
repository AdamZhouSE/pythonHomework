#include<iostream>
#include<stack>
#include<vector>
const int maxn = 2e5+5;

using namespace std;

int low[maxn],dfn[maxn],ans=maxn,n,index,vis[maxn];
vector<int> Edge[maxn];
stack<int> S;//tarjan 用栈 

void tarjan(int u)
{
    low[u]=dfn[u]=++index;
    vis[u] = 1;
    S.push(u);
    for(int i=0;i<Edge[u].size();i++)
    {
        int v = Edge[u][i];
        if(!dfn[v])
        {
            tarjan(v);
            low[u] = min(low[u],low[v]);
        }
        else if(vis[v])
            low[u] = min(low[u],dfn[v]); 
    }
    if(low[u]==dfn[u])
    {
        int count = 0,now;
        while(1)
        {
            count++;//记录点的个数 
            now = S.top();
            vis[now] = 0;
            S.pop();
            if(now == u)
                break;
        }
        if(count > 1)//只有一个点不视为强连通分量 
        {
            ans = min(count,ans);
        }
    }
}

int main()
{
    cin >> n;
    for(int i=1;i<=n;i++)
    {
        int x;
        cin >> x;
        Edge[i].push_back(x);
    }
    for(int i=1;i<=n;i++)
    {
        if(!dfn[i])
            tarjan(i);
    }
    cout << ans;
    return 0;
}
