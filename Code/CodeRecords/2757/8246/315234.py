#include <cstdio>
#include <iostream>
#include <cstring>
#define N 700
using namespace std;
int n, eid;
short sz[N+5], head[N+5];
struct Edge 
{
    int next, to;
}e[2*N+5];
struct bign
{
    static const int maxn = 120;
    short d[maxn+5];
    short len;
    void clean() { while(len > 1 && !d[len-1]) len--; }
    bign() { memset(d, 0, sizeof(d)); len = 1; }
    bign(int num) { *this = num; } 
    bign(char* num) { *this = num; }
    bign operator = (const char* num) {
        memset(d, 0, sizeof(d)); len = strlen(num);
        for(int i = 0; i < len; i++) d[i] = num[len-1-i] - '0';
        clean();
        return *this;
    }
    bign operator = (int num)
    {
        char s[20]; sprintf(s, "%d", num);
        *this = s;
        return *this;
    }
    bign operator + (const bign& b)
    {
        bign c = *this; int i;
        for(i = 0; i < b.len; i++)
        {
            c.d[i] += b.d[i];
            if (c.d[i] > 9) c.d[i] %= 10, c.d[i+1]++;
        }
        while (c.d[i] > 9) c.d[i++] %= 10, c.d[i]++;
        c.len = max(len, b.len);
        if (c.d[i] && c.len <= i) c.len = i+1;
        return c;
    }
    bign operator - (const bign& b)
    {
        bign c = *this; int i;
        for(i = 0; i < b.len; i++)
        {
            c.d[i] -= b.d[i];
            if (c.d[i] < 0) c.d[i] += 10, c.d[i+1]--;
        }
        while (c.d[i] < 0) c.d[i++] += 10, c.d[i]--;
        c.clean();
        return c;
    }
    bign operator * (const bign& b) const
    {
        int i, j; bign c; c.len = len + b.len; 
        for(j = 0; j < b.len; j++)
            for(i = 0; i < len; i++) 
                c.d[i+j] += d[i]*b.d[j];
        for(i = 0; i < c.len-1; i++) c.d[i+1] += c.d[i]/10, c.d[i] %= 10;
        c.clean();
        return c;
    }
    bign operator / (const bign& b)
    {
        int i, j;
        bign c = *this, a = 0;
        for(i = len - 1; i >= 0; i--)
        {
            a = a*10 + d[i];
            for (j = 0; j < 10; j++) 
                if (a < b*(j+1)) break;
            c.d[i] = j;
            a = a - b*j;
        }
        c.clean();
        return c;
    }
    bign operator % (const bign& b)
    {
        int i, j;
        bign a = 0;
        for(i = len - 1; i >= 0; i--) {
            a = a*10+d[i];
            for(j = 0; j < 10; j++) if (a < b*(j+1)) break;
            a = a-b*j;
        }
        return a;
    }
    bign operator += (const bign& b)
    {
        *this = *this+b;
        return *this;
    }
    bool operator <(const bign& b) const
    {
        if(len != b.len) return len < b.len;
        for(int i = len-1; i >= 0; i--)
            if(d[i] != b.d[i]) return d[i] < b.d[i];
        return false;
    }
    bool operator >(const bign& b) const { return b < *this; }
    bool operator <= (const bign& b) const { return !(b < *this); }
    bool operator >= (const bign& b) const { return !(*this < b); }
    bool operator != (const bign& b) const { return b < *this || *this < b; }
    bool operator == (const bign& b) const { return !(b < *this) && !(b > *this); }
    string str() const {
        char s[maxn] = {};
        for(int i = 0; i < len; i++) s[len-1-i] = d[i]+'0';
        return s;
    }
}f[N+5][N+5];
istream& operator >> (istream& in, bign& x)
{
    string s;
    in >> s;
    x = s.c_str();
    return in;
}
ostream& operator << (ostream& out, const bign& x)
{
    out << x.str();
    return out;
}
void addEdge(int u, int v) 
{
    e[++eid].next = head[u];
    e[eid].to = v;
    head[u] = eid;
}
void dp(int u, int fa) 
{
    sz[u] = 1, f[u][0] = f[u][1] = 1;
    for(int i = head[u]; i; i = e[i].next)
    {
        int v = e[i].to;
        if(v == fa) continue;
        dp(v, u);
        sz[u] += sz[v];
        for(int j = sz[u]; j >= 1; --j) 
        {
            for(int k = min(j, sz[u]-sz[v]); k >= max(1, j-sz[v]); --k)
            {
                f[u][j] = max(f[u][j], f[u][k]*f[v][j-k]);
            }
        }
    }
    for(int i = 1; i <= sz[u]; ++i) f[u][0] = max(f[u][0], f[u][i]*i);
}
int main() 
{
    scanf("%d",&n);
    for(int i = 1, x, y; i <= n-1; ++i)
    {
        scanf("%d %d",&x,&y);
        addEdge(x, y);
        addEdge(y, x);
    } 
    dp(1, 0);
    cout << f[1][0] << endl;
    return 0;
}