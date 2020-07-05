#include<iostream>

#include<cstdio>

#include<cstring>

#include<algorithm>

#include<cmath>

#include<vector>

#include<queue>

using namespace std;

inline int read()

{

	int x=0,f=1; char ch=getchar();

	while (ch<'0' || ch>'9') {if (ch=='-') f=-1; ch=getchar();}

	while (ch>='0' && ch<='9') {x=x*10+ch-'0'; ch=getchar();}

	return x*f;

}

#define MAXN 100010

#define LL long long

 

int N,M,K;

LL Dist,Num;

 

vector<int> G[MAXN];

 

namespace Graph{

	

	struct EdgeNode{

		int next,to,dis,from;

	}edge[MAXN<<1];

	int head[MAXN],cnt;

 

	inline void AddEdge(int u,int v,int w) {cnt++; edge[cnt].next=head[u]; head[u]=cnt; edge[cnt].to=v; edge[cnt].from=u; edge[cnt].dis=w;}

	inline void InsertEdge(int u,int v,int w) {AddEdge(u,v,w); AddEdge(v,u,w);}

 

	#define Pa pair<int,int>

	#define MP make_pair

	#define INF 0x7fffffff

	priority_queue<Pa,vector<Pa>,greater<Pa> >q;

	int dist[MAXN];

	inline void Dijkstra(int S=1)

	{

		for (int i=1; i<=N; i++) dist[i]=INF;

		q.push(MP(0,S)); dist[S]=0;

		while (!q.empty()) {

			int dis=q.top().first;

			int now=q.top().second;

			q.pop();

			if (dis>dist[now]) continue;

			for (int i=head[now]; i;i=edge[i].next) {

				if (dist[edge[i].to]>dis+edge[i].dis) {

					dist[edge[i].to]=dis+edge[i].dis;

					q.push(MP(dist[edge[i].to],edge[i].to));

				}

			}

		}

		

		for (int i=1; i<=cnt; i++) {

			int u=edge[i].from,v=edge[i].to,d=edge[i].dis;

			if (dist[u]+d==dist[v]) G[u].push_back(v);

		}

		

//		for (int i=1; i<=N; printf("Now=%d\n",i),i++)

//			for (int j=0; j<G[i].size(); j++)

//				printf("%d  ",G[i][j]);

	}

}

 

namespace TreeDivide{

 

	struct EdgeNode{

		int next,to,dis;

	}edge[MAXN<<1];

	int head[MAXN],cnt;

	

	inline void AddEdge(int u,int v,int w) {cnt++; edge[cnt].next=head[u]; head[u]=cnt; edge[cnt].to=v; edge[cnt].dis=w;}

	inline void InsertEdge(int u,int v,int w) {/*printf("<%d  %d>\n",u,v,w);*/ AddEdge(u,v,w); AddEdge(v,u,w);}

	

	int size[MAXN],mx[MAXN],root,Sz;

	bool visit[MAXN];

	inline void Getroot(int now,int last)

	{

		size[now]=1; mx[now]=0;

		for (int i=head[now]; i; i=edge[i].next)

			if (edge[i].to!=last && !visit[edge[i].to]) {

				Getroot(edge[i].to,now);

				size[now]+=size[edge[i].to];

				mx[now]=max(mx[now],size[edge[i].to]);

			}

		mx[now]=max(mx[now],Sz-size[now]);

		if (mx[now]<mx[root]) root=now;

	}

	

	int f[MAXN][2],g[MAXN][2];

	inline void DFS(int now,int last,int dep,int dis)

	{

		if (dep>K) return;

		if (dis>f[dep][0]) 

			f[dep][0]=dis,f[dep][1]=1;

		else 

			if (dis==f[dep][0]) 

				f[dep][1]++;

 

		for (int i=head[now]; i; i=edge[i].next)

			if (edge[i].to!=last && !visit[edge[i].to]) {

				DFS(edge[i].to,now,dep+1,dis+edge[i].dis);

			}

	}

	

	inline void Divide(int now)

	{

		visit[now]=1;

		for (int i=1; i<=K; i++) g[i][0]=g[i][1]=0;

		g[0][0]=0; g[0][1]=1;

		

		K--;

		for (int i=head[now]; i; i=edge[i].next)

			if (!visit[edge[i].to]) {

				

				for (int j=1; j<=K; j++) f[j][0]=f[j][1]=0;

				

				DFS(edge[i].to,now,1,edge[i].dis);

				

				for (int j=1; j<=K; j++) {

					if (Dist<g[K-j][0]+f[j][0])

						Dist=g[K-j][0]+f[j][0],Num=(LL)g[K-j][1]*f[j][1];

					else

						if (Dist==g[K-j][0]+f[j][0])

							Num+=(LL)g[K-j][1]*f[j][1];

				}

				

				for (int j=1; j<=K; j++) {

					if (g[j][0]<f[j][0])

						g[j][0]=f[j][0],g[j][1]=f[j][1];

					else

						if (g[j][0]==f[j][0])

							g[j][1]+=f[j][1];

				}

			}

		K++;

		

		

		for (int i=head[now]; i; i=edge[i].next) 

			if (!visit[edge[i].to]) {

				root=0;

				Sz=size[edge[i].to];

				Getroot(edge[i].to,now);

				Divide(root);

			}

	}

	

	bool mark[MAXN];

	inline void BuildTree(int now)

	{

		mark[now]=1;

		sort(G[now].begin(),G[now].end());

		for (int i=0; i<G[now].size(); i++) 

			if (!mark[G[now][i]]) {

			BuildTree(G[now][i]);

			InsertEdge(now,G[now][i],Graph::dist[G[now][i]]-Graph::dist[now]);

		}

	}

}using namespace TreeDivide;

 

int main()

{

	N=read(),M=read(),K=read();

	for (int i=1,x,y,z; i<=M; i++) {

		x=read(),y=read(),z=read();

		Graph::InsertEdge(x,y,z);

	}

	Graph::Dijkstra();

	TreeDivide::BuildTree(1);

	

	Sz=mx[root=0]=N;

	TreeDivide::Getroot(1,0);

	TreeDivide::Divide(root);

 

	printf("%lld %lld\n",Dist,Num);

	return 0;

}