#include<algorithm>
#include<cstring>
#include<vector>
#include<unordered_map>
#define ll unsigned long long
#define MAXN 400005
#define MAXT 10000005
#define MAXM 4000005
using namespace std;
const int LIM=50;
const ll sd=1234321237;

int N,K,Q;ll Ans[MAXN];char A[MAXN];

int srt,las,tot,mx[MAXN],par[MAXN][20],son[MAXN][27],pos[MAXN];
int rt[MAXN],ls[MAXT],rs[MAXT],sz[MAXT],seg_tot,seg_n;

ll ha[MAXN],hb[MAXN],pw[MAXN];
int nex[MAXN][LIM+3],id[MAXN][LIM+3],ori_beg[MAXT],id_tot;
unordered_map<ll,int>las_pos;
vector<int>save[MAXM];ll sum[MAXN];int D[MAXN];

int En[MAXN],Nex[MAXN],Las[MAXN],Tot;
int EN[MAXM],NEX[MAXM],LAS[MAXM],TOT;

void (int x,int y){
	En[++Tot]=y;
	Nex[Tot]=Las[x];
	Las[x]=Tot;
}

void ADD(int x,int y){
	EN[++TOT]=y;
	NEX[TOT]=LAS[x];
	LAS[x]=TOT;
}

struct node{
	int s,t,l,r,len,id;
}ask[MAXN];int ask_tot;
bool operator<(node a,node b){
	return a.s>b.s;
}

void modify(int &p,int l,int r,int k){
	if(!p)p=++seg_tot;sz[p]++;
	if(l==r)return;
	int mid=l+r>>1;
	if(k<=mid)modify(ls[p],l,mid,k);
	else modify(rs[p],mid+1,r,k);
}

int Merge(int x,int y,int l,int r){
	if(!x||!y)return x|y;
	int p=++seg_tot,mid;
	if(l==r){
		sz[p]=sz[x]+sz[y];
		return p;
	}
	mid=l+r>>1;
	ls[p]=Merge(ls[x],ls[y],l,mid);
	rs[p]=Merge(rs[x],rs[y],mid+1,r);
	sz[p]=sz[ls[p]]+sz[rs[p]];
	return p;
}

int findnext(int p,int l,int r,int k){
	if(k>N||sz[p]==0)return -1;
	if(l==r)return k<=l?l:-1;
	int mid=l+r>>1,ret=-1;
	if(l>=k&&sz[ls[p]])return findnext(ls[p],l,mid,k);
	if(mid>=k){
		if(sz[ls[p]])ret=findnext(ls[p],l,mid,k);
		if(~ret)return ret;
		return findnext(rs[p],mid+1,r,k);
	}
	return findnext(rs[p],mid+1,r,k);
}

int push(int val){
	mx[++tot]=val;
	return tot;
}

void extend(int t){
	int p,q,np,nq;
	np=push(mx[las]+1);
	for(p=las;p&&!son[p][t];p=par[p][0])son[p][t]=np;
	if(!p)par[np][0]=srt;
	else{
		q=son[p][t];
		if(mx[q]==mx[p]+1)par[np][0]=q;
		else{
			nq=push(mx[p]+1);
			memcpy(son[nq],son[q],sizeof(son[q]));
			par[nq][0]=par[q][0];
			par[q][0]=par[np][0]=nq;
			for(;son[p][t]==q;p=par[p][0])son[p][t]=nq;
		}
	}
	las=np;
}

int jump(int p,int d){
	for(int i=19;i>=0;i--)if(mx[par[p][i]]>=d)p=par[p][i];
	return p;
}

void dfs(int x){
	int i,y;
	for(i=1;i<20;i++)par[x][i]=par[par[x][i-1]][i-1];
	for(i=Las[x];i;i=Nex[i]){
		y=En[i];
		dfs(y);
		rt[x]=Merge(rt[x],rt[y],1,seg_n);
	}
}

void sam_init(){
	int i;
	seg_n=N;
	for(i=2;i<=tot;i++)add(par[i][0],i);
	for(i=1;i<=N;i++)modify(rt[pos[i]],1,seg_n,i);
	dfs(1);
}

ll solve1(int s,int t,int l,int r){
	ll ret=0;int len=r-l+1,cur,p;
	p=jump(pos[N+1+r],len);
	cur=findnext(rt[p],1,seg_n,s+len-1);
	while(cur<=t&&cur!=-1){
		ret+=(ll)K-(cur-len+1);
		cur=findnext(rt[p],1,seg_n,cur+len);
	}
	return ret;
}



ll gethash(ll h[],int l,int r){
	return h[r]-h[l-1]*pw[r-l+1];
}

void solve2(int x,int dep){
	int i,j,d,p,y,r;
	ll ret;
	for(j=0;j<save[x].size();j++){
		p=save[x][j];
		ret=0;d=dep;r=ask[p].t-ask[p].len+1;
		for(i=19;i>=0;i--)if((d>=(1<<i))&&ori_beg[D[d-(1<<i)]]<=r){
			ret+=sum[d]-sum[d-(1<<i)];
			d-=(1<<i);
		}
		if(ori_beg[D[d]]<=r&&d)ret+=sum[d]-sum[d-1];
		Ans[ask[p].id]=ret;
	}
	
	for(i=LAS[x];i;i=NEX[i]){
		y=EN[i];
		sum[dep+1]=sum[dep]+K-ori_beg[y];
		D[dep+1]=y;
		solve2(y,dep+1);
	}
}

//part 2

int main(){
	int i,j,k,s,t,l,r,tmp;
	ll hh;
	
	srt=las=push(0);
	scanf("%d%d",&N,&K);
	
	for(i=1,pw[0]=1;i<=N;i++)pw[i]=pw[i-1]*sd;
	scanf("%s",A+1);
	for(i=1;i<=N;i++)extend(A[i]-'a'),pos[i]=las;
	for(i=1;i<=N;i++)ha[i]=ha[i-1]*sd+A[i];
	extend(26);
	scanf("%s",A+1);
	for(i=1;i<=N;i++)extend(A[i]-'a'),pos[i+N+1]=las;
	for(i=1;i<=N;i++)hb[i]=hb[i-1]*sd+A[i];
	
	sam_init();
	
	scanf("%d",&Q);
	for(i=1;i<=Q;i++){
		scanf("%d%d%d%d",&s,&t,&l,&r);
		if(s+(r-l+1)>t)continue;
		if(r-l+1<=LIM){
			ask_tot++;
			ask[ask_tot]=(node){s,t,l,r,r-l+1,i};
			las_pos[gethash(hb,l,r)]=N+1;
		}
		else Ans[i]=solve1(s,t,l,r);
	}
	
	sort(ask+1,ask+ask_tot+1);
	for(i=1;i<=LIM;i++)nex[N+1][i]=N+1;
	j=N+1;
	
	for(i=1;i<=ask_tot;i++){
		while(j>ask[i].s){
			j--;
			for(k=1;k<=min(LIM,N-j+1);k++){
				hh=gethash(ha,j,j+k-1);
				if(!las_pos.count(hh))continue;
				id[j][k]=++id_tot;ori_beg[id_tot]=j;
				
				tmp=las_pos[hh];
				nex[j][k]=tmp;
				while(tmp<=j+k-1)tmp=nex[tmp][k];
				ADD(id[tmp][k],id[j][k]);
				las_pos[hh]=j;
			}
		}
		hh=gethash(hb,ask[i].l,ask[i].r);
		s=las_pos[hh];
		if(s+ask[i].len-1>ask[i].t)continue;
		save[id[s][ask[i].len]].push_back(i);
	}
	
	ori_beg[0]=N+1;
	solve2(0,0);
	
	for(i=1;i<=Q;i++)printf("%llun",Ans[i]);
}