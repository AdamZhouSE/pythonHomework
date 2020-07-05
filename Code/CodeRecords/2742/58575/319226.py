#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cctype>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <cmath>
#define pk putchar(' ')
#define ph puts("")
#pragma GCC optimize(2)
using namespace std;
typedef long long ll;
template <class T>
void rd(T &x)
{
    x = 0;
    int f = 1;
    char c = getchar();
    while (!isdigit(c)) {if (c == '-') f = -1; c = getchar();}
    while (isdigit(c)) x = (x << 3) + (x << 1) + (c ^ 48), c = getchar();
    x *= f;
}
template <class T>
void pt(T x)
{
    if (x < 0)
        putchar('-'), x = (~x) + 1;
    if (x > 9)
        pt(x / 10);
    putchar(x % 10 ^ 48);
}
template <class T>
T Max(T a, T b)
{
    return a > b ? a : b;
}
template <class T>
T Min(T a, T b)
{
    return a < b ? a : b;
}
using namespace std;
const int INF = 0x3f3f3f3f, N = 5e5 + 5;
int n, rt[N];
struct Node 
{
    int val, rnd, siz, l ,r;
};
struct Treapnode
{
    Node t[N * 50];
    int tot;
    void New(int &p, int x)
    {
        p = ++tot;
        t[p].val = x;
        t[p].siz = 1;
        t[p].rnd = rand();
    }
    void update(int p)
    {
        t[p].siz = t[t[p].l].siz + t[t[p].r].siz + 1;
    }

    int merge(int a,int b)
    {
        if (!a || !b)
            return a + b;
        if (t[a].rnd > t[b].rnd)
        {
            int p = ++tot;
            t[p] = t[a];
            t[p].r = merge(t[p].r, b);
            update(p);
            return p;
        }
        else
        {
            int p = ++tot;
            t[p] = t[b];
            t[p].l = merge(a, t[p].l);
            update(p);
            return p;
        }
    }

    void split(int p, int k, int& x, int& y) 
    {
        if (!p) 
            return (void)(x = y = 0); 
        if (t[p].val <= k) 
        {
            x = ++tot;
            t[x] = t[p];
            split(t[x].r, k, t[x].r, y);
            update(x);
        }
        else 
        {
            y = ++tot;
            t[y] = t[p];
            split(t[y].l, k, x, t[y].l);
            update(y);
        }
    }
  
    void ins(int& p, int x) 
    {
        int a = 0, b = 0, c = 0;
        split(p, x, a, b);
        New(c, x);
        p = merge(merge(a, c), b);
    }
  
    void del(int& p, int x) 
    {
        int a = 0, b = 0, c = 0;
        split(p, x, a, c);
        split(a, x - 1, a, b);
        b = merge(t[b].l, t[b].r);
        p = merge(merge(a, b), c);
    }

    int get_rank(int& p, int x) 
    {
        int a, b, c;
        split(p, x - 1, a, b);
        c = t[a].siz + 1;
        p = merge(a, b);
        return c;
    }
    int get_val(int p, int x)
    {
        if (x == t[t[p].l].siz + 1)
            return t[p].val;
        else if (x <= t[t[p].l].siz)
            return get_val(t[p].l, x);
        else 
            return get_val(t[p].r, x - t[t[p].l].siz - 1);
    }
    int pre(int& p, int x) 
    {
        int a, b, c;
        split(p, x - 1, a, b);
        if (!a)
            return -2147483647;
        c = get_val(a, t[a].siz);
        p = merge(a, b);
        return c;
    }

    int sub(int& p, int x) 
    {
        int a, b, c;
        split(p, x, a, b);
        if (!b)
            return 2147483647;
        c = get_val(b, 1);
        p = merge(a, b);
        return c;
    }

}Treap;
int main() 
{

    rd(n);
    int tim, opt, x;
    for (int i = 1;i <= n; i++)
    {
        rd(tim), rd(opt), rd(x);
        rt[i] = rt[tim];
        switch(opt)
        {
            case 1: Treap.ins(rt[i], x); break;
            case 2: Treap.del(rt[i], x); break;
            case 3: pt(Treap.get_rank(rt[i], x)), ph; break;
            case 4: pt(Treap.get_val(rt[i], x)), ph; break;
            case 5: pt(Treap.pre(rt[i], x)), ph; break;
            case 6: pt(Treap.sub(rt[i], x)), ph; break;
        }
    }
    return 0;
}
