#include<bits/stdc++.h>
#define llt long long
#define N 100005
using namespace std;
int n,m,Tcnt,Ecnt,lastans;
int root[N*20],rank[N],deep[N];
int head[N];
int fa[N][25];
struct tyq1{
	int ty1,ty2;
}a[N];
struct tyq2{
	int left,right,sz;
}tyee[N*20];
struct tyq3{
	int to,next;
}tybuff[2*N];
bool cmp(tyq1 x,tyq1 y){
	return x.ty1<y.ty1;
}
void add(int x,int y){
	tybuff[++Ecnt].to=y;
	tybuff[Ecnt].next=head[x];
	head[x]=Ecnt;
}
void insert(int &num,int &x,int L,int R){
	tyee[Tcnt++]=tyee[x];
	x=Tcnt-1;	tyee[x].sz++;
	if (L==R)	return;
	int mid=(L+R)>>1;
	if (num<=mid) insert(num,tyee[x].left,L,mid);
		else	insert(num,tyee[x].right,mid+1,R);
}
void dfs(int x,int y){
	root[x]=root[y];
	insert(rank[x],root[x],1,n);
	for (int tt=head[x];tt;tt=tybuff[tt].next){
		int z=tybuff[tt].to;
		if (z==y) continue;
		deep[z]=deep[x]+1;
		fa[z][0]=x;
		dfs(z,x);
	}
}
int lca(int x,int y){
	if (deep[x]<deep[y]) swap(x,y);
	int t=deep[x]-deep[y];
	for (int i=0;i<=16;i++)
		if (t&(1<<i))	x=fa[x][i];
	for (int i=16;i>=0;i--)
		if (fa[x][i]!=fa[y][i])
			x=fa[x][i],y=fa[y][i];
	if (x==y)	return x;
		else return fa[x][0];
}
int query(int ll,int rr,int fa1,int fafa1,int k,int L,int R){
	if (L==R)	return L;
	int tmp=tyee[tyee[rr].left].sz+tyee[tyee[ll].left].sz
			-tyee[tyee[fa1].left].sz-tyee[tyee[fafa1].left].sz;
	int mid=(L+R)>>1;
	if (tmp>=k)	return query(tyee[ll].left,tyee[rr].left,tyee[fa1].left,tyee[fafa1].left,
							k,L,mid);
		else	return query(tyee[ll].right,tyee[rr].right,tyee[fa1].right,tyee[fafa1].right,
							k-tmp,mid+1,R);
}
int main(){
	scanf("%d%d",&n,&m);
	for (int i=1;i<=n;i++){
		scanf("%d",&a[i].ty1);
		a[i].ty2=i;
	}
	sort(a+1,a+1+n,cmp);
	for (int i=1;i<=n;i++)	rank[a[i].ty2]=i;
	int x,y; Ecnt=0;
	for (int i=1;i<n;i++){
		scanf("%d%d",&x,&y);
		add(x,y); add(y,x);
	}
	Tcnt=1; root[0]=0;
	dfs(1,0);
	
	for (int j=1;j<=16;j++)
		for (int i=1;i<=n;i++)
			if ((1<<j)<=deep[i]) fa[i][j]=fa[fa[i][j-1]][j-1];
 
	int xx,yy,zz;
	lastans=0;
	for (int i=1;i<=m;i++){
		scanf("%d%d%d",&xx,&yy,&zz);
		xx^=lastans;
		int tyqiang=lca(xx,yy);
		int tyqq=fa[tyqiang][0];
		int tmp=query(root[xx],root[yy],root[tyqiang],root[tyqq],zz,1,n);
		printf("%d",a[tmp].ty1);
		lastans=a[tmp].ty1;
		printf("\n");
        
	}
	return 0;
}

