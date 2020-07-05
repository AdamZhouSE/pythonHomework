#include<stdio.h>
#include<string.h>
#include<stack>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> G[10005], Gn[10005];
stack<int> st;
int t, num, n, low[10005], time[10005], inst[10005], vis[10005], ltt[10005], cnt[10005];
void Trajan(int u);
int main(void)
{
	int m, i, j, u, v, now, ans;
	while(scanf("%d%d", &n, &m)!=EOF)
	{
		for(i=1;i<=n;i++)
		{
			G[i].clear();
			Gn[i].clear();
		}
		for(i=1;i<=m;i++)
		{
			scanf("%d%d", &u, &v);
			G[u].push_back(v);
		}
		memset(vis, 0, sizeof(vis));
		memset(cnt, 0, sizeof(cnt));
		t = num = 0;
		for(i=1;i<=n;i++)
		{
			if(vis[i]==0)
				Trajan(i);
		}
		while(st.empty()==0)
		{
			now = st.top();
			st.pop();
			ltt[now] = ++num;
			cnt[now] = 1;
			inst[now] = 0;
		}
		for(i=1;i<=n;i++)
		{
			for(j=0;j<G[i].size();j++)
			{
				v = G[i][j];
				if(ltt[i]!=ltt[v])
					Gn[ltt[i]].push_back(ltt[v]);
			}
		}
		ans = now = 0;
		for(i=1;i<=num;i++)
		{
			if(Gn[i].size()==0)
			{
				if(now==0)
					now = 1, ans = cnt[i];
				else
					ans = 0;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
 
void Trajan(int u)
{
	int i, v, now, sum;
	time[u] = low[u] = ++t;
	vis[u] = inst[u] = 1;
	st.push(u);
	for(i=0;i<G[u].size();i++)
	{
		v = G[u][i];
		if(vis[v]==0)
		{
			Trajan(v);
			low[u] = min(low[u], low[v]);
		}
		else if(inst[v]==1)
			low[u] = min(low[u], time[v]);
	}
	if(time[u]==low[u])
	{
		num++;
		sum = 0;
		while(st.empty()==0)
		{
			now = st.top();
			inst[now] = 0;
			ltt[now] = num;
			st.pop();
			sum++;
			if(now==u)
				break;
		}
		cnt[num] = sum;
	}
}