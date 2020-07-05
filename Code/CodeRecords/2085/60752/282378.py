#include <bits/stdc++.h>

 

using namespace std;

const int inf=2e9;

const int maxn=10010;

int n,m,root;

int head[1000],in[1000],pre[1000],vis[1000],id[1000];

long long ans;

 

struct node{

    int from,to,val;

}E[maxn];

 

 

long long mintree()

{

    while (1)

    {

        for (int i=1; i<=n; i++)

        {

            in[i]=inf;

        }

        for (int i=1; i<=m; i++)

        {

            if (E[i].from!=E[i].to&&E[i].val<in[E[i].to])

            {

                in[E[i].to]=E[i].val;

                pre[E[i].to]=E[i].from;

            }

        }

        for (int i=1; i<=n; i++)

        {

            if (in[i]==inf&&i!=root)

            {

                return -1;

            }

        }

        int cnt=0;

        memset(vis,0,sizeof(vis));

        memset(id,0,sizeof(id));

        in[root]=0;

        for (int i=1; i<=n; i++)

        {

            ans+=in[i];

            int v=i;

            while (vis[v]!=i&&id[v]==0&&v!=root)

            {

                vis[v]=i;

                v=pre[v];

            }

            //找环

            if (v!=root&&id[v]==0)

            {

                id[v]=++cnt;

                for (int u=pre[v]; u!=v; u=pre[u])

                {

                    id[u]=cnt;

                }

            }

            //对环进行收缩

        }

        if (!cnt)

        {

            break;

        }

        for (int i=1;i<=n;i++){

            if (!id[i]){

                id[i]=++cnt;

            }

        }

        for (int i=1;i<=m;i++){

            int u=E[i].from,v=E[i].to;

            E[i].from=id[E[i].from];

            E[i].to=id[E[i].to];

            if (u!=v){

                E[i].val-=in[v];

            }

        }//新建图

        n=cnt;

        root=id[root];

    }

    return ans;

}

int main()

{

    scanf("%d%d%d",&n,&m,&root);

    for (int i=1; i<=m; i++)

    {

        scanf("%d%d%d",&E[i].from,&E[i].to,&E[i].val);

    }

    cout<<mintree();

}