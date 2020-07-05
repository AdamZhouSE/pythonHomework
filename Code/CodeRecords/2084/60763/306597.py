#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;
inline int read(){
	register int x=0,f=0,ch=getchar();
	while('0'>ch||ch>'9')f^=ch=='-',ch=getchar();
	while('0'<=ch&&ch<='9')x=(x<<1)+(x<<3)+(ch^'0'),ch=getchar();
	return f?-x:x;
}
const int MAX=6505; 
int n,m,s,t,w,S,T;
struct E{
	int e,next,w;
}e[MAX<<1];
int cnt=1,head[MAX]; 
inline void add(int u,int v,int w){
	e[cnt]=(E){v,head[u],w};
	head[u]=cnt++;
}
priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int> > >q;
int dis[MAX],x,y,vis[MAX];
inline void dijkstra(int s){
	memset(dis,0x3f,sizeof(dis));
	dis[s]=0;q.push(make_pair(0,s));
	while(!q.empty()){
		x=q.top().second;q.pop();
		if(!vis[x]){
			vis[x]=1;
			for(register int i=head[x];i;i=e[i].next){
				if(dis[e[i].e]>dis[x]+e[i].w){
					dis[e[i].e]=dis[x]+e[i].w;
					if(!vis[e[i].e])q.push(make_pair(dis[e[i].e],e[i].e));
				}
			}
		} 
	}
}
signed main(){
	n=read();m=read();S=read(),T=read(); 
	for(register int i=1;i<=m;++i){
		s=read(),t=read(),w=read();
		add(s,t,w);add(t,s,w);
	}
	dijkstra(S);
	printf("%d\n",dis[T]);
	return 0;
}