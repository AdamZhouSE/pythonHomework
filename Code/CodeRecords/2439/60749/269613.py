#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 2e5 + 7;
int head[maxn],nex[maxn],to[maxn],val[maxn],tot;
int n,dat[maxn];

void init()
{
    for(int i = 1;i <= 2 * n;i++)head[i] = 0;
    tot = 0;
}

void add(int x,int y,int z)
{
    to[++tot] = y;
    nex[tot] = head[x];
    val[tot] = z;
    head[x] = tot;
}

void dfs(int u,int fa)
{
    for(int i = head[u];i;i = nex[i])
    {
        int v = to[i],w = val[i];
        if(v == fa)continue;
        dat[v] = dat[u] ^ w;
        dfs(v,u);
    }
}

int main()
{
    while(~scanf("%d",&n))
    {
        init();
        for(int i = 1;i < n;i++)
        {
            int x,y,z;scanf("%d%d%d",&x,&y,&z);
            add(x,y,z);add(y,x,z);
        }
        dfs(1,-1);

        int q;scanf("%d",&q);
        while(q--)
        {
            int x,y;scanf("%d%d",&x,&y);
            printf("%d\n",dat[x] ^ dat[y]);
        }
    }
    return 0;
}

