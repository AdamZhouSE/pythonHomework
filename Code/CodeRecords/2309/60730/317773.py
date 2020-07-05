#define _CRT_SECURE_NO_WARNINGS
#include <ctime>
#include <queue>
#include <cmath>
#include <cstdio>
#include <bitset>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define Maxi 100005
#define INF 0x3f3f3f3f
//#define Mod 10000
typedef long long ll;
char mp[Maxi];
bool vis[Maxi];
int match[Maxi];
int head[Maxi], tot;
struct Node {
    int Next, to;
} edge[Maxi << 1];
void add(int x, int y) {
    edge[++tot].to = y;
    edge[tot].Next = head[x];
    head[x] = tot;
}
int ver[Maxi];
bool DFS(int x) {
    for (int i = head[x], y; ~i; i = edge[i].Next) {
        if (!vis[y = edge[i].to]) {
            vis[y] = true;
            if (!match[y] || DFS(match[y])) {
                match[y] = x;
                return true;
            }
        }
    }
    return false;
}
int main() {
    ios::sync_with_stdio(0);
    int cnt, cnt1, cnt3;
    cnt = cnt1 = cnt3 = 0;
    int n, m, ans = 0;
    cin >> n >> m;
    memset(head, -1, sizeof(head[0]) * (n * m + 3));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++, cnt++) {
            cin >> mp[cnt];
            if (mp[cnt] == '2')
                ans++;
            else if (mp[cnt] == '1') {
                ver[cnt] = ++cnt1;
                if (i && mp[cnt - m] == '3')
                    add(cnt1, ver[cnt - m]);
                if (j && mp[cnt - 1] == '3')
                    add(cnt1, ver[cnt - 1]);
            } else if (mp[cnt] == '3') {
                ver[cnt] = ++cnt3;
                if (i && mp[cnt - m] == '1')
                    add(ver[cnt - m], cnt3);
                if (j && mp[cnt - 1] == '1')
                    add(ver[cnt - 1], cnt3);
            }
        }
    }
    for (int i = 1; i <= cnt1; i++) {
        memset(vis, false, sizeof(vis[0]) * (cnt3 + 1));
        if (DFS(i))
            ans++;
    }
    cout << ans << endl;
    return 0;
}