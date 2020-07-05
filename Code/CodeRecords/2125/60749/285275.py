#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
int n, m, k, sz[5005];
vector<pair<int, int> > ans;
int main() {
    scanf("%d", &k);
    while (sz[m] < k) ++m, sz[m] = m * (m - 1) >> 1;
    while (k) {
        while (sz[m] > k) --m;
        if (n)
            ans.push_back({ n, n + 1 });
        for (int i = 1; i < m; ++i) ans.push_back({ n + i, n + i + 1 });
        ans.push_back({ n + m, n + 1 });
        n += m;
        k -= sz[m];
    }
    printf("%d %d\n", n, (int)ans.size());
    for (auto x : ans) printf("%d %d\n", x.first, x.second);
    return 0;
}