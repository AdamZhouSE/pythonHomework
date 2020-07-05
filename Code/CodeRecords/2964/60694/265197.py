// https://loj.ac/submission/514309

#include <bits/stdc++.h>

using namespace std;

const int N = 210, M = 1e6 + 10, K = 10;

char buf[M], *s[N], *tmp = buf;
int n, len[N], dp[K * 2][K * 2], ans[K];

int work(int x, int y) {
    int t = 0;
    while (t < min(len[x], len[y]) && s[x][t] == s[y][t]) t++;
    if (t == len[x] && t == len[y])
        return 0;
    memset(dp, 128, sizeof(dp));
    dp[0][K] = t;
    // cout << t << " " << len[x] << " " << len[y] << endl;
    for (int i = 1; i <= 8; i++) {
        for (int j = -8; j <= 8; j++) {
            int t = -M;
            t = max(t, dp[i - 1][K + j - 1]);      // insert
            t = max(t, dp[i - 1][K + j + 1] + 1);  // erase
            t = max(t, dp[i - 1][K + j] + 1);      // modify
            int p = t;
            if (t + j < 0)
                continue;
            while (t < len[x] && t + j < len[y] && s[x][t] == s[y][t + j]) t++;
            dp[i][K + j] = t;
        }
        if (dp[i][K + len[y] - len[x]] == len[x])
            return i;
    }
    return 9;
}

int main() {
    cin >> n;
    for (int i = 1; i <= n; i++) {
        scanf("%s", tmp);
        s[i] = tmp;
        len[i] = strlen(s[i]);
        tmp += len[i] + 1;
    }
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            if (abs(len[i] - len[j]) > 8)
                continue;
            int w = work(i, j);
            // if (w == 1) cout << i + 1 << " " << j + 1 << endl;
            if (w <= 8)
                ans[w]++;
        }
    }
    for (int i = 1; i <= 8; i++) cout << ans[i] << " ";
    return 0;
}