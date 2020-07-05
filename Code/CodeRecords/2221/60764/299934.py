#include<map>
#include<cmath>
#include<ctime>
#include<queue>
#include<cstdio>
#include<vector>
#include<bitset>
#include<cstring>
#include<iostream>
#include<algorithm>
#define pa pair<int,int>
#define ll long long
#define inf 1000000000
using namespace std;
ll read()
{
    ll x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
int n, m, ind, top, scc, ans;
int dfn[10005], low[10005], inq[10005], q[10005], bl[10005], size[10005], d[10005];
int u[50005], v[50005];
vector<int> e[10005];
void tarjan(int x)
{
    dfn[x] = low[x] = ++ind;
    q[++top] = x;
    inq[x] = 1;
    for(int i = 0; i < e[x].size(); i++)
        if(!dfn[e[x][i]])
        {
            tarjan(e[x][i]);
            low[x] = min(low[x], low[e[x][i]]);
        }
        else if(inq[e[x][i]])
            low[x] = min(low[x], dfn[e[x][i]]);
    if(dfn[x] == low[x])
    {
        int now = -1; scc++;
        while(now != x)
        {
            now = q[top]; top--;
            inq[now] = 0;
            bl[now] = scc;
            size[scc]++;
        }
    }
}
int main()
{
    n = read(); m = read();
    for(int i = 1; i <= m; i++)
    {
        u[i] = read(), v[i] = read();
        e[v[i]].push_back(u[i]);
    }
    for(int i = 1; i <= n; i++)
        if(!dfn[i])
            tarjan(i);
    for(int i = 1; i <= m; i++)
        if(bl[u[i]] != bl[v[i]])
            d[bl[u[i]]]++;
    for(int i = 1; i <= scc; i++)
    {
        if(d[i] == 0)
        {
            if(ans)
            {
                ans = 0;
                break;
            }
            ans = size[i];            
        }
    }
    printf("%d\n", ans);
    return 0;
}