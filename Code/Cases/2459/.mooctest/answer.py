#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
const int maxn = 3e5 + 10;
ll sum;
int n, k, cnt = 1, w[maxn], ans[maxn];

priority_queue <pii> q;

int main() {
    scanf("%d %d", &n, &k);
    for (int i = 1; i <= n; i++) {
        scanf("%d", w + i);
    }
    for (int i = k + 1; i <= k + n; i++) {
        for (; cnt <= n && cnt <= i; ) {
            q.push(make_pair(w[cnt], cnt)), cnt++;
        }
        pii node = q.top();
        q.pop();
        ans[node.second] = i;
        sum += 1ll * node.first * (i - node.second);
    }
    printf("%lld\n", sum);
    for (int i = 1; i <= n; i++) {
        printf("%d ", ans[i]);
    }
    return 0;
}