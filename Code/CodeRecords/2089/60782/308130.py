#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cctype>
#include <cmath>
#include <queue>
#include <cstdlib>
#define R register
#define W while
#define gc getchar()
#define IN inline
#define MX 100005
#define INF 999999999
template <class T>
IN void in(T &x)
{
    x = 0; R char c = gc;
    W (!isdigit(c)) c = gc;
    W (isdigit(c))
    x = (x << 1) + (x << 3) + c - 48, c = gc;
}
std::queue <int> q;
std::priority_queue <int> qq;
int cnt, dot, line, k, deal, lef, rig, mx, root;
int head[MX], h[MX], dist[MX], fat[MX], dep[MX], siz[MX], sum[MX], que[MX], num[MX], val[MX];
long long ans1, ans2;
bool vis[MX];
struct Edge
{
    int to, len, nex;
}e[MX << 1], edge[MX << 1];
namespace SPFA
{
    IN void add(const int &from, const int &to, const int &len)
    {
        e[++cnt] = {to, len, h[from]};
        h[from] = cnt;
    }
    IN void addedge(const int &from, const int &to, const int &len)
    {
        edge[++cnt] = {to, len, head[from]};
        head[from] = cnt;
    }
    void spfa()
    {
        memset(dist, 63, sizeof(dist));
        R int now;
        q.push(1);
        dist[1] = 0;
        W (!q.empty())
        {
            now = q.front(); q.pop();
            for (R int i = h[now]; i; i = e[i].nex)
            {
                if(dist[e[i].to] >= dist[now] + e[i].len)
                {
                    if(dist[e[i].to] > dist[now] + e[i].len)
                    {
                        dist[e[i].to] = dist[now] + e[i].len;
                        if(!vis[e[i].to]) 
                        {
                            vis[e[i].to] = true;
                            q.push(e[i].to);
                        }
                    }
                }
            }
            vis[now] = false;
        }
    }
    void rebuild()
    {
        R int now;
        qq.push(-1); vis[1] = true;
        W (!qq.empty())
        {
            now = qq.top(), qq.pop(); now = -now;//优先队列编号大的在前面， 所以存成负数
            for (R int i = h[now]; i; i = e[i].nex)
            {
                if(vis[e[i].to] || dist[e[i].to] != dist[now] + e[i].len) continue;
                addedge(now, e[i].to, e[i].len), addedge(e[i].to, now, e[i].len), vis[e[i].to] = true, qq.push(-e[i].to);
            }
        }
    }
}
namespace Dot_Divide
{
    void reset() { for (R int i = 1; i <= k; ++i) val[i] = -INF, num[i] = 0; }
    void DFS(const int &now, const int &fa)
    {//统计子树大小
        siz[now] = 1;
        for (int i = head[now]; i; i = edge[i].nex)
        {
            if(edge[i].to == fa) continue;
            DFS(edge[i].to, now);
            siz[now] += siz[edge[i].to];
        }
    }
    void getroot(const int &now, const int &fa)
    {
        sum[now] = 0;
        for (R int i = head[now]; i; i = edge[i].nex)
        {
            if(vis[edge[i].to] || edge[i].to == fa) continue;
            getroot(edge[i].to, now);
            sum[now] = std::max(sum[now], siz[edge[i].to]);
        }
        sum[now] = std::max(sum[now], deal - siz[now]);
        if(sum[now] < mx) mx = sum[now], root = now;
    }
    void cal(const int &now)
    {
        int tar;
        for (R int j = head[now]; j; j = edge[j].nex)
        {
            if(vis[edge[j].to]) continue;
            dep[edge[j].to] = 1, dist[edge[j].to] = edge[j].len, fat[edge[j].to] = now;
            que[rig = 1] = edge[j].to, lef = 0;
            W (lef < rig)//手写队列存子树
            {
                ++lef; 
                for (R int i = head[que[lef]]; i; i = edge[i].nex)
                {
                    if(vis[edge[i].to] || edge[i].to == fat[que[lef]]) continue;
                    fat[edge[i].to] = que[lef], dep[edge[i].to] = dep[que[lef]] + 1, dist[edge[i].to] = dist[que[lef]] + edge[i].len;
                    if(dep[edge[i].to] >= k) break;
                    que[++rig] = edge[i].to;
                }
            }
            for (R int i = 1; i <= rig; ++i)//计算不同子树间的贡献
            {
                tar = dep[que[i]];
                if(dist[que[i]] + val[k - tar - 1] > ans1) ans1 = dist[que[i]] + val[k - tar - 1], ans2 = num[k - tar - 1];
                else if(dist[que[i]] + val[k - tar - 1] == ans1) ans2 += num[k - tar - 1];
            }
            for (R int i = 1; i <= rig; ++i)//更新最长路径长度和数量
            {
                tar = dep[que[i]];
                if(tar == k - 1)
                {
                    if(ans1 < dist[que[i]]) ans1 = dist[que[i]], ans2 = 1;//单独一条合法的链
                    else if(ans1 == dist[que[i]]) ans2++;
                    continue;
                }
                if(dist[que[i]] > val[tar]) val[tar] = dist[que[i]], num[tar] = 1;
                else if(dist[que[i]] == val[tar]) num[tar]++;
            }
        }
    }
    void solve(const int &now)
    {
        root = 0, mx = INF;
        getroot(now, 0);
        reset(); cal(root);
        vis[root] = true;
        for (int i = head[root]; i; i = edge[i].nex)
        {
            if(vis[edge[i].to]) continue;
            deal = siz[edge[i].to], solve(edge[i].to);
            //乍一看直接把处理的子树大小改成以1为根的子树大小有点问题， 其实这个问题只在子树中包含1节点的情况下存在，而多dfs一遍显然加大常数， 所以直接用此信息
        }
    }
}
int main(void)
{
    int a, b, c;
    in(dot), in(line), in(k);
    for (R int i = 1; i <= line; ++i)
    {
        in(a), in(b), in(c);
        SPFA::add(a, b, c), SPFA::add(b, a, c);
    }
    SPFA::spfa(), SPFA::rebuild(), Dot_Divide::DFS(1, 0);
    deal = dot;
    memset(vis, false, sizeof(vis));
    Dot_Divide::solve(1);
    printf("%lld %lld\n", ans1, ans2);
}