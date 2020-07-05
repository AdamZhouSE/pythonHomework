#include<bits/stdc++.h>
#include<cstdio>
using namespace std;
int num,dfn[600001],low[600001],l=1,n,m,cut=0,toto[600001],root,ans=0,zre[600001],anss[600001];
bool war[600001],kk[5001][5001];
stack<int>lon;
struct road{
	int to,next;
}a[1000001];
void join(int p,int q){
	a[++num].to=q; 
	a[num].next=toto[p];
	toto[p]=num;
}
void tarjan(int x,int k){
	dfn[x]=low[x]=l++;
	war[x]=1;
	lon.push(x);
	for(int i=toto[x];i;i=a[i].next){
		int y=a[i].to;
		if(k==y)continue;
		if(!dfn[y]){
			tarjan(y,x);
			low[x]=min(low[x],low[y]);
		}
		else if(war[y])low[x]=min(low[x],dfn[y]);
	}
	if(dfn[x]==low[x]){
		cut++;
		while(lon.top()!=x){
			war[lon.top()]=0;
			zre[lon.top()]=cut;
			lon.pop();
		}
		war[lon.top()]=0;
		zre[lon.top()]=cut;
		lon.pop();
	}
}
void find_leaf(int q){
	for(int i=toto[q];i;i=a[i].next){
	    int p=a[i].to;
	    if(zre[q]!=zre[p]&&!kk[zre[q]][zre[p]]&&!kk[zre[p]][zre[q]]){
	    	anss[zre[q]]++;
	    	anss[zre[p]]++;
	    	kk[zre[q]][zre[p]]=1;
	    	kk[zre[p]][zre[q]]=1;
		}
	}
}
int main(){
	scanf("%d%d",&n,&m);
	num=0;
	for(int i=1;i<=m;++i){
		int x,y;
		scanf("%d%d",&x,&y);
		join(x,y);
		join(y,x);
	}
	for(int i=1;i<=n;++i){
		if(!dfn[i])tarjan(i,0);
	}
	for(int i=1;i<=n;++i)
        find_leaf(i);
	for(int i=1;i<=n;++i)
        if(anss[i]==1)ans++;
	printf("%d\n",(ans+1)/2);
	return 0;
}
