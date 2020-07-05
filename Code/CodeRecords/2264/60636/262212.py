#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int inf = 0x3f3f3f3f;
const int N = 1000 + 5;
const int M = 1005;
int head[N], ver[M], nxt[M], dfn[N], low[N], st[N], cut[N], sta[N];
int top, tot, cnt, num;
int n, m, root;
vector<int> dcc[N];

void init(){
    memset(head, 0, sizeof head);
    memset(low, 0, sizeof low);
    memset(dfn, 0, sizeof dfn);
    memset(cut, 0, sizeof cut);
    memset(sta, 0, sizeof sta);
    num = top = cnt = 0;
    for (int i = 0; i < N;i++)
        dcc[i].clear();
    tot = 1;
}
void add(int x,int y){
    ver[++tot] = y, nxt[tot] = head[x], head[x] = tot;
}
void tarjan(int x){
    dfn[x] = low[x] = ++num;
    st[++top] = x;
    if(x == root && head[x] == 0){ // 孤立点
        dcc[++cnt].push_back(x);
        return ;
    }
    int flag = 0;
    for(int i=head[x];i;i=nxt[i]){
        int y = ver[i];
        if(!dfn[y]){
            tarjan(y);
            low[x] = min(low[x], low[y]);
            if(low[y] >= dfn[x]){
                flag ++;
                if(x != root || flag > 1)cut[x] = true;
                cnt++;
                int z;
                do{
                    z = st[top--];
                    dcc[cnt].push_back(z);
                }while(z != y);
                dcc[cnt].push_back(x);
            }
        }else low[x] = min(low[x], dfn[y]);
    }
}
int main() {
    int cas = 0;
    while(~scanf("%d",&m)){
        if(m == 0)
            break;
        init();
        int maxn = 0;
        for (int i = 1; i <= m; i++) {
            int x, y;
            scanf("%d%d", &x, &y);
            add(x, y);
            add(y, x);
            sta[x] = sta[y] = 1;
            maxn = max(maxn, max(x, y));
        }
        int res1 = 0;
        ull res2 = 1;
        for (int i = 1; i <= maxn;i++){
            if(!dfn[i] && sta[i]){
                root = i;
                tarjan(i);
            }
            else if(sta[i] == 0) res1++;
        }
        for (int i = 1; i <= cnt;i++){
            int now = 0;
            for (int j = 0; j < dcc[i].size();j++){
                if(cut[dcc[i][j]])
                    now++;
            }
            if(now > 1) continue;
            else if(now == 1){
                res1++;
                res2 *= (dcc[i].size() - 1);
            } else {
                res1 += 2;
                res2 *= (dcc[i].size() * (dcc[i].size() - 1)) / 2;
            }
        }
        printf("Case %d: %d %llu\n", ++cas, res1, res2);
    }
    return 0;
}