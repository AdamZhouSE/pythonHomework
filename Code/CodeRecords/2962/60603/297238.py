
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
using namespace std;
const int maxn = 1e6;
bool vis[maxn];
string s;
int n, p;
map<string, int> m;
int main() {
    scanf("%d %d", &n, &p);
    memset(vis, false, sizeof(vis));
    for (int i = 1; i <= n; i++) {
        cin >> s;
        int len = s.size();
        int x = 0;
        if (len == 1) x = (s[0]-'A');
        else if (len == 2) x = 32*(s[0]-'A')+(s[1]-'A');
        else  {
            for (int j = 3; j >= 1; j--) {
                int t = len - j;
                x = x * 32 + s[t] - 'A';
            }
        }
        x = x % p;
        if (m[s] || !vis[x]) {
            m[s] = x;
            vis[x] = true;
            cout << x;
        }
        else {
            int y;
            for (int j = 1; j*j < maxn; j++) {
                y = (x+j*j) % p;
                if (!vis[y]) {
                    vis[y] = true;
                    m[s] = y;
                    printf("%d", y);
                    break;
                }
                y = (x-j*j+p) % p;
                if (!vis[y]) {
                    vis[y] = true;
                    m[s] = y;
                    printf("%d", y);
                    break;
                }
            }
        }
        if (i < n) cout << " ";
        else printf("\n");
    }
    return 0;
}
