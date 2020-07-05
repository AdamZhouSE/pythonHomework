#include<queue>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define N 10005
#define M 200005
using namespace std;
int n,m,k,t,p,q;
int val[N],d[N][25],first[N],v[M],w[M],nxt[M];
int Abs(int x)  {return x>0?x:-x;}
void add(int x,int y,int z){
	nxt[++t]=first[x],first[x]=t,v[t]=y,w[t]=z;
}
struct node{
	int x,del,dis;
	node(int x=0,int del=0,int dis=0):x(x),del(del),dis(dis){}
};
bool operator<(const node &p,const node &q)  {return p.dis>q.dis;}
priority_queue<node>Q;
void dijkstra(int S){
	memset(d,0x3f,sizeof(d));
	Q.push(node(S,val[S]+k,0)),d[S][val[S]+k]=0;
	while(!Q.empty()){
		node now=Q.top();Q.pop();
		for(int i=first[now.x];i;i=nxt[i]){
			int to=v[i],num=now.del+val[to];
			if(num<0||num>2*k)  continue;
			if(d[to][num]>now.dis+w[i]){
				d[to][num]=now.dis+w[i];
				Q.push(node(to,num,d[to][num]));
			}
		}
	}
}
int main(){
	int x,y,z,T;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d%d",&n,&m,&k);
		t=0,memset(first,0,sizeof(first));
		for(int i=1;i<=n;++i)  scanf("%d",&x),val[i]=(x==1)?1:-1;
		for(int i=1;i<=m;++i){
			scanf("%d%d%d",&x,&y,&z);
			add(x,y,z),add(y,x,z);
		}
		scanf("%d%d",&p,&q),dijkstra(p);
		int ans=0x3f3f3f3f;
		for(int i=0;i<=2*k;++i)  ans=min(ans,d[q][i]);
		printf("%d\n",ans==0x3f3f3f3f?-1:ans);
	}
	return 0;
}
