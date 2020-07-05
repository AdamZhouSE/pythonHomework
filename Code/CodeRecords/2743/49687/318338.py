#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

const int maxn = 300050;
const int maxm = maxn << 1;
int N, M;
int a[maxn], t1, t2;
int head[maxn], cnt;

struct Edge{
    int u, v, next;
}edge[maxm];

inline void addedge(int u, int v){
    edge[++cnt].u = u;
    edge[cnt].v = v;
    edge[cnt].next = head[u];
    head[u] = cnt;
}

int fa[maxn][31], dep[maxn];

void dfs(int u, int faa){
    fa[u][0] = faa, dep[u] = dep[faa] + 1;
    for(int i = 1; i <= 30; i++){
        fa[u][i] = fa[ fa[u][i - 1] ][i - 1];
    }
    for(int i = head[u]; i ; i = edge[i].next){
        int v = edge[i].v;
        if(v == faa)continue;
        dfs(v, u);
    }
} 

inline int lca(int x, int y){
    if(dep[x] < dep[y])swap(x,y);
    for(int i = 30; i >= 0; i--){
        if(dep[ fa[x][i] ] >= dep[y]) x = fa[x][i];
    }
    if(x == y)return x;
    for(int i = 30; i >= 0; i--){
        if(fa[x][i] != fa[y][i]){
            x = fa[x][i], y = fa[y][i];
        }
    }
    return fa[x][0];
}

int num[maxn];

int answer(int u, int faa){
    for(int i = head[u]; i ; i = edge[i].next){
        int v = edge[i].v;
        if(v == faa)continue;
        answer(v, u);
        num[u] += num[v];
    }
}
int main(){
    cin>>N;
    for(int i = 1; i <= N; i++){
        cin>> a[i];
    }
    for(int i = 1; i < N; i++){
        cin>> t1>> t2;
        addedge(t1, t2);
        addedge(t2, t1);
    }
    dfs(1, 0);
    for(int i = 1; i <= N - 1; i++){
        int u = a[i], v = a[i + 1];
        int t = lca(u, v);
        num[ fa[t][0] ] -= 1;
        num[ t ] -= 1;
        num[ u ] += 1;
        num[ v ] += 1;
    }
    answer(1,0);
    for(int i = 2; i <= N; i++){
        num[a[i]]--;
    }
    for(int i = 1; i <= N; i++){
        cout<<num[i]<<endl;
    }
}