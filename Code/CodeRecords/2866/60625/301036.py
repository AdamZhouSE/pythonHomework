#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
#include<ctype.h>
#include<math.h>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<bitset>
#include<algorithm>
#include<time.h>
using namespace std;
void fre() { freopen("c://test//input.in", "r", stdin); freopen("c://test//output.out", "w", stdout); }
#define MS(x,y) memset(x,y,sizeof(x))
#define MC(x,y) memcpy(x,y,sizeof(x))
#define MP(x,y) make_pair(x,y)
#define ls o<<1
#define rs o<<1|1
typedef long long LL;
typedef unsigned long long UL;
typedef unsigned int UI;
template <class T1, class T2>inline void gmax(T1 &a, T2 b) { if (b>a)a = b; }
template <class T1, class T2>inline void gmin(T1 &a, T2 b) { if (b<a)a = b; }
const int N = 0, M = 0, Z = 1e9 + 7, ms63 = 0x3f3f3f3f;
int n;
int x;
int b[105];
int main()
{
	while (~scanf("%d", &n))
	{
		int m = 0;
		for (int i = 1; i <= n; ++i)
		{
			scanf("%d", &x);
			if (x == 1)b[++m] = i;
		}
		if (m == 0)puts("0");
		else
		{
			LL ans = 1;
			for (int i = 1; i < m; ++i)
			{
				ans = ans*(b[i + 1] - b[i]);
			}
			printf("%lld\n", ans);
		}
	}
	return 0;
}
/*
【trick&&吐槽】
1，这题最坏情况下，ans可达2^48*3，会爆int。
2，还是需要考虑没有1这种无法划分的特殊情况。
【题意】
有n（1<=n<=100）个数，每个数不是0，就是1.
我们要把这些数划分成若干区间段。使得每个区间段恰好都有且仅有一个1
问你划分的方案数
【类型】
简单题
【分析】
显然，有多少个1，我们就必然要划分成多少段。
然后，两个相邻1之间有w个0，我们的划分方案数就是w+1
于是，我们记录所有1的位置，对于任意一对相邻的1，答案乘上b[i+1]-b[i]
然后就AC啦
【时间复杂度&&优化】
O(n)
*/