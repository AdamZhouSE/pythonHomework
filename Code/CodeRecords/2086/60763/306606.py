#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int maxN=200005,maxM=500005;
int fa[maxN],n,m,tot;
struct Edge {int frm,to,val;friend bool operator < (Edge a,Edge b) {return a.val<b.val;}}edge[maxM];
namespace ufs {
void init(int n) {/*srand(time(NULL));*/for (int i=1;i<=n;i++) fa[i]=i;}
int find(int x) {return fa[x]==x?x:fa[x]=find(fa[x]);}
//void merge(int x,int y) {(rand()&1?fa[find(x)]=find(y):fa[find(y)]=find(x));} 
}
char buf[20000],*S,*T;
char gc();
void rd(int&),kr(); 
int main() {
	rd(n),rd(m);
	ufs::init(n);
	for (int i=1;i<=m;i++) rd(edge[i].frm),rd(edge[i].to),rd(edge[i].val);
	sort(edge+1,edge+m+1);kr();
	return 0;
}
char gc() {
	if (S==T) {T=(S=buf)+fread(buf,1,50000,stdin);if (S==T) return EOF;}
	return *S++;
}
void rd(int& x) {
	x=0;char ch=getchar();
	while (!isdigit(ch)) ch=getchar();
	while (isdigit(ch)) {x=x*10+ch-48;ch=getchar();}
}
void kr() {
	ll ans=0;
	for (int i=1;i<=m;i++) {
		int fx=ufs::find(edge[i].frm),fy=ufs::find(edge[i].to);
		if (fx!=fy) {
			ans+=edge[i].val;
			fa[fx]=fy;
			if (++tot==n-1) break;
		}
	}
	cout<<ans;
}