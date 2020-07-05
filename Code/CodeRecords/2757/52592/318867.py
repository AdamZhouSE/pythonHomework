#include<cstdio>
#include<cmath>
#include<queue>
#include<stack>
#include<vector>
#include<algorithm>
#include<cstring>
#include<iostream>
using namespace std;
 
typedef long long LL;
 
const int INF = 2147483647;
const int maxn = 710;
const int r = 1000000000;
 
struct data{
	int tot;
	LL m[20]; data(){memset(m,0,sizeof(m)); tot = 1;}
	data operator * (data b) const
	{
		data ret;
		for (int i = 1; i <= tot; i++)
		{
			for (int j = 1; j <= b.tot; j++)
			{
				ret.m[i + j] += (ret.m[i + j - 1] + m[i] * b.m[j]) / r;
				ret.m[i + j - 1] = (ret.m[i + j - 1] + m[i] * b.m[j]) % r;
			}
		}
		ret.tot = tot + b.tot - 1;
		while (ret.m[ret.tot + 1])
		{
			ret.tot++;
			ret.m[ret.tot + 1] += ret.m[ret.tot] / r;
			ret.m[ret.tot] = ret.m[ret.tot] % r;
		}
		return ret;
	}
	data operator & (LL b) const
	{
		data ret;
		for (int i = 1; i <= tot; i++)
		{
			ret.m[i + 1] += (ret.m[i + 1] + m[i] * b) / r;
			ret.m[i] = (ret.m[i] + m[i] * b) % r;
		}
		ret.tot = tot;
		while (ret.m[ret.tot + 1])
		{
			ret.tot++;
			ret.m[ret.tot + 1] += ret.m[ret.tot] / r;
			ret.m[ret.tot] = ret.m[ret.tot] % r;
		}
		return ret;
	}
};
 
vector<int> e[maxn];
LL n,siz[maxn],s[maxn];
data f[maxn][maxn],ff[maxn],g[maxn];
 
inline LL getint()
{
	LL ret = 0,f = 1;
	char c = getchar();
	while (c < '0' || c > '9')
	{
		if (c == '-') f = -1;
		c = getchar();
	}
	while (c >= '0' && c <= '9')
		ret = ret * 10 + c - '0',c = getchar();
	return ret * f;
}
 
inline data hmax(data a,data b)
{
	if (a.tot < b.tot) return b;
	if (b.tot < a.tot) return a;
	for (int i = a.tot; i >= 1; i--)
	{
		if (a.m[i] > b.m[i]) return a;
		if (a.m[i] < b.m[i]) return b;
	}
	return a;
}
 
inline void dp(int u,int fa)
{
	siz[u]++;
	for (int i = 0; i < e[u].size(); i++)
	{
		int v = e[u][i];
		if (v == fa) continue;
		dp(v,u);
		siz[u] += siz[v];
		for (int j = 0; j <= siz[u]; j++) ff[j] = f[u][j];
		for (int j = 0; j <= siz[u] - 1; j++)
			for (int k = 0; k <= min(1ll * j,siz[u] - siz[v]); k++)
				f[u][j] = hmax(f[u][j],f[v][j - k] * ff[k]);
	}
	for (LL j = 0; j <= siz[u] - 1; j++)
		f[u][siz[u]] = hmax(f[u][siz[u]],f[u][j] & (siz[u] - j));
}
 
inline void init()
{
	for (int i = 1; i <= n; i++) 
		f[i][0].m[1] = 1;
}
 
inline void print(data a)
{
	int cnt,pos;
	for (int i = 1; i <= a.tot; i++)
	{
		cnt = 0; pos = (i - 1) * 9;
		while (a.m[i])
		{
			s[++pos] = a.m[i] % 10;
			a.m[i] /= 10;
		}
	}
	for (int i = pos; i >= 1; i--) {
        cout<<s[i];}
    cout<<endl;
}
 
int main()
{
	n = getint();
	for (int i = 1; i <= n - 1; i++)
	{
		int u = getint(),v = getint();
		e[u].push_back(v); e[v].push_back(u);
	}
	init();
	dp(1,0);
	print(f[1][n]);
	return 0;
}
