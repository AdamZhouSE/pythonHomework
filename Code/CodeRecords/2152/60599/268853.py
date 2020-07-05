#include <cstdio>
#include <queue>
#include <stack>
using namespace std;
#define MAXN 200005
queue < int > q;
stack < int > sta;
int n;
int d[MAXN], f[MAXN], orz[MAXN], ans[MAXN];
bool vis[MAXN];

void Top_sort () {
	for ( int i = 1;i <= n;i ++ )
		if ( ! d[i] )
			q.push ( i );
	while ( ! q.empty() ) {
		int t = q.front();
		q.pop();
		sta.push( t );
		d[f[t]] --;
		if ( ! d[f[t]] )
			q.push( f[t] );
	}
}
void dfs ( int u, int root ) {
	if ( vis[u] )
		return;
	vis[u] = 1;
	ans[root] += orz[u];
	q.push( u );
	dfs ( f[u], root );
}
void circle () {
	for ( int i = 1;i <= n;i ++ )
		if ( d[i] && ! vis[i] ) {
			dfs ( i, i );
			while ( ! q.empty() ) {
				int t = q.front();
				q.pop();
				ans[t] = ans[i];
			}
		}
}

int main() {
	scanf ( "%d", &n );
	for ( int i = 1;i <= n;i ++ )
		scanf ( "%d", &orz[i] );
	for ( int i = 1;i <= n;i ++ ) {
		scanf ( "%d", &f[i] );
		d[f[i]] ++;
	}
	Top_sort ();
	circle ();
	while ( ! sta.empty() ) {
		int t = sta.top();
		sta.pop();
		ans[t] = orz[t] + ans[f[t]];
	}
	for ( int i = 1;i <= n;i ++ )
		printf ( "%d\n", ans[i] );
	return 0;
} 