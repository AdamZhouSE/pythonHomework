#include <cstdio>
#include <map>
const int maxn = 100010;
int n, m, tot = 1, last = 1;
#define ll long long
ll ans;
int len[maxn << 1], fa[maxn << 1];
std::map<int, int> ch[maxn << 1];
int calc(int x) { return len[x] - len[fa[x]]; }
void insert(int x) {
  int p = last, np = last = ++tot;
  len[np] = len[p] + 1;
  while (p && !ch[p][x])
    ch[p][x] = np, p = fa[p];
  if (!p)
    fa[np] = 1, ans += calc(np);
  else {
    int q = ch[p][x];
    if (len[p] + 1 == len[q])
      fa[np] = q, ans += calc(np);
    else {
      int nq = ++tot;
      len[nq] = len[p] + 1;
      ch[nq] = ch[q];
      fa[nq] = fa[q];
      ans += calc(nq) - calc(q);
      fa[q] = fa[np] = nq;
      ans += calc(np) + calc(q);
      while (p && ch[p][x] == q)
        ch[p][x] = nq, p = fa[p];
    }
  }
}
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    int x;
    scanf("%d", &x);
    insert(x);
    printf("%lld\n", ans);
  }
}