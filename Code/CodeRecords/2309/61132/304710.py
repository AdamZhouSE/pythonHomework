#include<bits/stdc++.h>
#define pb push_back
using namespace std;
inline int read(){
	int res=0,f=1;char ch=getchar();
	while(!isdigit(ch)) {if(ch=='-') f=-f;ch=getchar();}
	while(isdigit(ch)) {res=(res<<1)+(res<<3)+(ch^48);ch=getchar();}
	return res*f;
}
int n,m;
inline int index(int x,int y){return y+(x-1)*m;}
namespace Dinic{
	const int N=4e5+5,INF=1e9;
	int vis[N<<1],head[N<<1],nxt[N<<1],c[N<<1],tot=1;
	inline void add(int x,int y,int z){
		vis[++tot]=y;nxt[tot]=head[x];head[x]=tot;c[tot]=z;
		vis[++tot]=x;nxt[tot]=head[y];head[y]=tot;c[tot]=0;
	}
	int d[N];
	int s,t;
	inline bool bfs(){
		memset(d,-1,sizeof(d));
		queue<int>q;
		q.push(s);d[s]=1;
		while(!q.empty()){
			int x=q.front();q.pop();
			for(int i=head[x];i;i=nxt[i]){
				int y=vis[i];
				if(c[i] && d[y]==-1){
					q.push(y);d[y]=d[x]+1;
					if(y==t) return 1;
				}
			}
		}
		return 0;
	}
	inline int dfs(int v,int flow){
		if(v==t) return flow;
		int res=flow,k;
		for(int i=head[v];i && res;i=nxt[i]){
			int y=vis[i];
			if(d[y]==d[v]+1 && c[i]){
				k=dfs(y,min(res,c[i]));
				if(!k) d[y]=-1;
				c[i]-=k;c[i^1]+=k;res-=k;
				if(!flow) break;
			}
		}
		return flow-res;
	}
	inline int dinic(){
		int flow,mxflow=0;
		while(bfs())	
			while(flow=dfs(s,INF)) mxflow+=flow;
		return mxflow;
	}
}
using namespace Dinic;
vector<int>a[N>>2];
inline void build(){
	for(int i=1;i<=n;i++)
		for(int j=0;j<m;j++){
			if(a[i][j]==1){
				add(s,index(i,j+1),1);
				if(i!=1) if(a[i-1][j]==3) add(index(i,j+1),index(i-1,j+1),1);
				if(i!=n) if(a[i+1][j]==3) add(index(i,j+1),index(i+1,j+1),1);
				if(j!=0) if(a[i][j-1]==3) add(index(i,j+1),index(i,j),1);
				if(j!=m-1) if(a[i][j+1]==3) add(index(i,j+1),index(i,j+2),1);
			}
			else if(a[i][j]==3) add(index(i,j+1),t,1);
		}
}
char ch[N];
int main(){
	n=read(),m=read();
	s=0,t=n*m+1;
	int ans=0;
	for(int i=1;i<=n;i++){
		scanf("%s",ch);
		for(int j=1;j<=m;j++){
			if(ch[j-1]=='2') ++ans,a[i].pb(0);
			else if(ch[j-1]=='*') a[i].pb(0);
			else if(ch[j-1]=='1') a[i].pb(1);
			else a[i].pb(3);
		}
	}
	build();
	cout<<ans+dinic()<<endl;
	return 0;
}
————————————————
版权声明：本文为CSDN博主「romiqi_new」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_43346903/article/details/99650409