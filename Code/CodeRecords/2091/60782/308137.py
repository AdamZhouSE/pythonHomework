#include <cstdio>
#include <cstring>
#include <vector>

int n,m,i,q[1010],rt,t1,t2;
bool vis[1010];
std::vector <int> u[1010];

bool f(int v) {
    for (int i=0;i<u[v].size();i++)
    if (!vis[rt = u[v][i]]) {
        vis[rt] = true;
        if ((!q[rt]) || f(q[rt])) return q[rt] = v;
    } return false;
}

int main() {
    scanf("%d%d",&n,&m);
    for (i=1;i<=m;i++) {
        scanf("%d%d",&t1,&t2);
        u[i].push_back(t1);  u[i].push_back(t2);
    }
    for (i=1;i<=m;i++) if (memset(vis,0,sizeof(vis)) && !f(i)) break;
    printf("%d\n",i - 1);
}