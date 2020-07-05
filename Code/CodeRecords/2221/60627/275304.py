#include<stdio.h>
#include<iostream>
using namespace std;
const int N=10005;
struct stack{
	int t,a[N];
	void clear(){
		t=0;
	}
	bool empty(){
		return !t;
	}
	void push(int x){
		a[t++]=x;
	}
	void pop(){
		--t;
	}
	int top(){
		return a[t-1];
	}
}t;
struct edge{
	int v,next;
}e[N*5];
int head[N],pre[N],low[N],scc[N],sum[N],num[N],dfs_clock,s,k;
void add(int u,int v){
	++k;
	e[k].v=v;
	e[k].next=head[u];
	head[u]=k;
}
void dfs(int u){
	pre[u]=low[u]=++dfs_clock;
	t.push(u);
	int i,v;
	for(i=head[u];i;i=e[i].next){
		v=e[i].v;
		if(!pre[v]){
			dfs(v);
			low[u]=min(low[u],low[v]);
		}
		else{
			if(!scc[v]){
				low[u]=min(low[u],pre[v]);
			}
		}
	}
	if(low[u]==pre[u]){
		++s;
		do{
			v=t.top();
			t.pop();
			scc[v]=s;
		}while(u!=v);
	}
}
int main(){
	int n,m,i,j,ans=-1;
	scanf("%d%d",&n,&m);
	while(m--){
		scanf("%d%d",&i,&j);
		add(i,j);
	}
	for(i=1;i<=n;i++){
		if(!pre[i]){
			dfs(i);
		}
	}
	for(i=1;i<=n;i++){
		num[scc[i]]++;
		for(j=head[i];j;j=e[j].next){
			if(scc[i]!=scc[e[j].v]){
				sum[scc[i]]++;
			}
		}
	}
	for(i=1;i<=s;i++){
		if(!sum[i]){
			if(ans==-1){
				ans=num[i];
			}
			else{
				ans=0;
				break;
			}
		}
	}
	printf("%d\n",ans);
	return 0;
}