#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
using namespace std;
#define rep(i, s, t) for(int i = (s); i <= (t); i++)
#define dwn(i, s, t) for(int i = (s); i >= (t); i--)
int read() {
    int x = 0, f = 1; char c = getchar();
    while(!isdigit(c)){ if(c == '-') f = -1; c = getchar(); }
    while(isdigit(c)){ x = x * 10 + c - '0'; c = getchar(); }
    return x * f;
}
#define maxn 50
#define oo 2147483647
int n, A[maxn], cnt, l[maxn], r[maxn];
struct Data {
    int C[maxn];
    void add(int x, int v) {
        for(; x <= n; x += x & -x) C[x] += v;
        return ;
    }
    int sum(int x) {
        int ans = 0;
        for(; x; x -= x & -x) ans += C[x];
        return ans;
    }
    int que(int l, int r) {
        if(l > r) return 0;
        return sum(r) - sum(l - 1);
    }
} up, dwn;
int ans;
void dfs(int now, int nans) {
    if(nans >= ans) return ;
    if(now > cnt) return (void)(ans = nans);
    up.add(r[now], 1);
    dfs(now + 1, nans + min(up.que(l[now], r[now] - 1), up.que(r[now] + 1, n) + dwn.que(l[now], n)));
    up.add(r[now], -1);
    dwn.add(r[now], 1);
    dfs(now + 1, nans + min(dwn.que(l[now], r[now] - 1), dwn.que(r[now] + 1, n) + up.que(l[now], n)));
    dwn.add(r[now], -1);
    return ;
}
int main() {
    int T = read();
    while(T--) {
        n = read();
        rep(i, 1, n) A[i] = read();
        cnt = 0;
        rep(i, 1, n) rep(j, i + 1, n) if(A[j] == A[i]) l[++cnt] = i, r[cnt] = j;
        ans = oo;
        dfs(1, 0);
        printf("%d\n", ans);
    }
    return 0;
}