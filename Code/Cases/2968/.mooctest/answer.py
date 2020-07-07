#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <vector>
using namespace std;
namespace mine {
typedef long long ll;
#define pr pair<int, int>
#define FR first
#define SE second
#define MP make_pair
#define PB push_back
#define vc vector
#define lc 2 * x
#define rc 2 * x + 1
#define mid (l + r) / 2
void chmax(int &x, const ll y) { x = (x > y ? x : y); }
void chmin(int &x, const ll y) { x = (x < y ? x : y); }
ll qread() {
    ll ans = 0, f = 1;
    char c = getchar();
    while (c < '0' or c > '9') {
        if (c == '-')
            f = -1;
        c = getchar();
    }
    while ('0' <= c and c <= '9') ans = ans * 10 + c - '0', c = getchar();
    return ans * f;
}
void write(ll num) {
    if (num < 0)
        putchar('-'), num = -num;
    if (num >= 10)
        write(num / 10);
    putchar('0' + num % 10);
}
void write1(ll num) {
    write(num);
    putchar(' ');
}
void write2(ll num) {
    write(num);
    putchar('\n');
}
const int INF = 0x3f3f3f3f;
const int MOD = 19930726;
void add(ll &a, ll b) {
    a += b;
    if (a >= MOD)
        a -= MOD;
    if (a <= -MOD)
        a += MOD;
}
ll qpower(ll x, int e) {
    ll ans = 1;
    while (e) {
        if (e & 1)
            ans = ans * x % MOD;
        x = x * x % MOD;
        e >>= 1;
    }
    return ans;
}
ll invm(ll x) { return qpower(x, MOD - 2); }
const int N = 1e6 + 10;

char str[N];
int id, lst[2];
struct Nod {
    int son[26], fail, dep, len;
} p[N];
int node(int len) {
    p[++id].len = len;
    return id;
}
int fl, fr;
ll ans = 0;
int gg(int pp, int pos, int op) {
    while (str[pos + (op == 1 ? (-1 - p[pp].len) : (1 + p[pp].len))] != str[pos]) pp = p[pp].fail;
    return pp;
}
void insert(int pos, int c, int op) {
    int pp = gg(lst[op], pos, op);
    if (!p[pp].son[c]) {
        int now = node(p[pp].len + 2);
        p[pp].son[c] = now;
        p[now].fail = (pp ? p[gg(p[pp].fail, pos, op)].son[c] : 1);
        p[now].dep = p[p[now].fail].dep + 1;
        if (p[now].len == fr - fl + 1)
            lst[op ^ 1] = now;
    }
    ans += p[lst[op] = p[pp].son[c]].dep;
}
char tmp[N];
void main() {
    id = -1;
    node(-1);
    node(0);
    fl = N / 2, fr = fl - 1;
    scanf("%s", tmp + 1);
    int ln = strlen(tmp + 1);
    for (int i = 1; i <= ln; i++) str[++fr] = tmp[i], insert(fr, tmp[i] - 'a', 1);

    int q = qread();
    while (q--) {
        int op = qread();
        if (op == 3)
            write2(ans);
        else {
            scanf("%s", tmp + 1);
            int ln = strlen(tmp + 1);
            for (int i = 1; i <= ln; i++)
                if (op == 1)
                    str[++fr] = tmp[i], insert(fr, tmp[i] - 'a', 1);
                else
                    str[--fl] = tmp[i], insert(fl, tmp[i] - 'a', 0);
        }
    }
}
};  // namespace mine
int main() {
    srand(time(0));
    mine::main();
}