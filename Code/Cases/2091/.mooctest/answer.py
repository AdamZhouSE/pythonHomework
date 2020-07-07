#include <bits/stdc++.h>
using namespace std;
#define N 1010
int rt[N][N];
int card[N];
int used[N];
int n, m;
int dfs(int x) {
    for (int i = 0; i < n; i++)
        if (rt[x][i] && !used[i]) {
            used[i] = true;
            if (card[i] == -1 || dfs(card[i])) {
                card[i] = x;
                return 1;
            }
        }
    return 0;
}
int main() {
    memset(rt, 0, sizeof(rt));
    memset(card, -1, sizeof(card));
    cin >> n >> m;  // n is card m is problem
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        rt[i][a] = 1;
        rt[i][b] = 1;
    }
    int ans = 0;
    for (int i = 0; i < m; i++)  //题目为主元
    {
        memset(used, 0, sizeof(used));
        if (dfs(i))
            ans++;
        else
            break;
    }
    cout << ans << endl;
    return 0;
}