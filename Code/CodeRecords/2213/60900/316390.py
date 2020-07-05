#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
inline int readint(){
	int a = 0, f = 1; char c = getchar();
	for(; c<'0' or c>'9'; c=getchar())
		if(c == '-') f = -1;
	for(; '0'<=c and c<='9'; c=getchar())
		a = (a<<3)+(a<<1)+(c^48);
	return a*f;
}

const int MaxN = 1000;
int n, m, q;
struct Query{
	int L, R, S, T, id;
	void input(){
		L = readint(), R = readint();
		S = readint(), T = readint();
	}
	bool operator<(const Query &that)const{
		return L < that.L;
	}
}query[200001];
struct Edge{
	int one, two;
	void input(){
		one = readint(), two = readint();
	}
};
Edge ppl[200001];

void init(){
	n = readint(), m = readint(), q = readint();
	for(int i=1; i<=m; ++i)
		ppl[i].input();
	for(int i=1; i<=q; ++i){
		query[i].input();
		query[i].id = i;
	}
	sort(query+1,query+q+1);
}

int dp[MaxN+1][MaxN+1];
bool answers[200001];
void solve(){
	for(int i=1; i<=n; ++i)
		for(int j=1; j<=n; ++j)
			dp[i][j] = (1<<20);
	int nowq = q;
	for(int i=m,x,y; i; --i){
		x = ppl[i].one, y = ppl[i].two;

		dp[x][y] = min(dp[x][y],i);
		dp[y][x] = min(dp[y][x],i);
		for(int j=1; j<=n; ++j){
			if(j != x) dp[y][j] = min(dp[y][j],dp[x][j]);
			if(j != y) dp[x][j] = min(dp[x][j],dp[y][j]);
		}
		while(nowq and query[nowq].L == i){
			answers[query[nowq].id] = (dp[query[nowq].S][query[nowq].T] <= query[nowq].R);
			-- nowq;
		}
	}
	for(int i=1; i<=q; ++i){
		if(answers[i]){
			putchar('Y');
			putchar('e');
			putchar('s');
		}
		else{
			putchar('N');
			putchar('o');
		}
		putchar('\n');
	}
}

int main(){
	// freopen("travel.in","r",stdin);
	// freopen("travel.out","w",stdout);
	init();
	solve();
	return 0;
}