#include<bits/stdc++.h>
using namespace std;
const int N=2e5+5;
//#pragma GCC optimize(2)
#define ms(a) memset(a,0,sizeof(a))
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
int n,m,bl[N],ans[N],pr[N],sf[N],va,st[N],ed[N],vv[N];
set<int>ss;
struct sa{
	char s[N];
	int sa[N],t[N],t2[N],c[N],lg[N],mn[20][N];
	int h[N],rk[N];
	void bd(int m){
		int *x=t,*y=t2;
		fo(i,0,m)c[i]=0;
		fo(i,1,n)c[x[i]=s[i]]++;
		fo(i,0,m)c[i]+=c[i-1];
		fd(i,n,1)
			sa[c[x[i]]--]=i;
		for(int k=1;k<=n;k*=2){
			int p=0;
			fo(i,n-k+1,n)y[++p]=i;
			fo(i,1,n)if(sa[i]>k)y[++p]=sa[i]-k;
			fo(i,0,m)c[i]=0;
			fo(i,1,n)c[x[y[i]]]++;
			fo(i,0,m)c[i]+=c[i-1];
			fd(i,n,1)sa[c[x[y[i]]]--]=y[i];
 			swap(x,y);p=1;x[sa[1]]=1;
			fo(i,2,n)
				x[sa[i]]=y[sa[i-1]]==y[sa[i]]&&y[sa[i-1]+k]==y[sa[i]+k]?p:++p;
			if(p>=n)break;m=p;
		}
	}
	void gh(){
		int j,k=0;
		fo(i,1,n)rk[sa[i]]=i;
		fo(i,1,n){
			if(k)k--;
			j=sa[rk[i]-1];
			while(s[i+k]==s[j+k]&&i+k<=n&&j+k<=n)k++;
			h[rk[i]]=k;
		}
		fo(i,2,2e5)lg[i]=lg[i>>1]+1;
		fo(i,1,n)mn[0][i]=h[i];
		fo(i,1,19)fo(j,1,n+1-(1<<i))
			mn[i][j]=min(mn[i-1][j],mn[i-1][j+(1<<(i-1))]);
	}
	int q(int l,int r){
		//l=rk[l];r=rk[r];
		if(l<1||r>n||l==r)return 0;
		if(l>r)swap(l,r);
		l++;
		int v=lg[r-l+1];
		return min(mn[v][l],mn[v][r-(1<<v)+1]);
	}
	void cl(){
		ms(sa);ms(rk);ms(h);
		ms(t);ms(t2);ms(c);ms(s);
		ms(mn);
	}
}s;
struct no{
	int l,r,i;
}a[N];
int operator <(no x,no y){
	return bl[x.l]<bl[y.l]||(bl[x.l]==bl[y.l]&&x.r>y.r);
}
void init(){
	for(int i=1;i<=n;i++){
		pr[i]=i-1;
		sf[i]=i+1;
	}
	sf[0]=1;
	pr[n+1]=n;
}
void is(int x){
	va=max(va,max(s.q(pr[x],x),s.q(sf[x],x)));
	sf[pr[x]]=x;
	pr[sf[x]]=x;
}
void dl(int x){
	pr[sf[x]]=pr[x];
	sf[pr[x]]=sf[x];
}
int main(){
	cin>>n>>m;
	cin>>s.s+1;
	reverse(s.s+1,s.s+n+1);
	s.bd(110);
	s.gh();
	int p=1,v=0;
	st[1]=1;
	for(int i=1;i<=n;i++){
		v++;
		bl[i]=p;
		if(v==(int)sqrt(n)){
			ed[p]=i;
			p++;
			st[p]=i+1;
			v=0;
		}
	}
	if(!ed[p])ed[p]=n;
	for(int i=1;i<=m;i++){
		cin>>a[i].l>>a[i].r;
		a[i].l=n-a[i].l+1;
		a[i].r=n-a[i].r+1;
		swap(a[i].l,a[i].r);
		a[i].i=i;
	}
	sort(a+1,a+m+1);
	int l=1,r=n;
	init();
	for(int i=1;i<=m;i++){
		if(a[i].l==a[i].r)continue;
		if(bl[a[i].l]==bl[a[i].r]){
			ss.clear();
			int va=0;
			for(int j=a[i].l;j<=a[i].r;j++){
				set<int>::iterator i1=ss.upper_bound(s.rk[j]);
				if(ss.empty()){
					ss.insert(s.rk[j]);
					continue;
				}
				if(i1==ss.begin()){
					va=max(va,s.q(*i1,s.rk[j]));
					ss.insert(s.rk[j]);
					continue;
				}
				i1--;
				set<int>::iterator i2=i1;
				i1++;
				if(i1==ss.end()){
					va=max(va,s.q(*i2,s.rk[j]));
					ss.insert(s.rk[j]);
					continue;
				}
				va=max(va,s.q(*i1,s.rk[j]));
				va=max(va,s.q(*i2,s.rk[j]));
				ss.insert(s.rk[j]);
			}
			ss.clear();
			ans[a[i].i]=va;
			continue;
		}
		if(bl[a[i].l]!=bl[a[i-1].l]){
			init();
			r=n;
			while(st[l+1]<=a[i].l)l++;
			for(int j=1;j<ed[l];j++)dl(s.rk[j]);
			for(int j=n;j>ed[l];j--)dl(s.rk[j]);
			va=0;
			for(int j=ed[l]+1;j<=n;j++){
				is(s.rk[j]);
				vv[j]=va;
			}
			for(int j=ed[l]-1;j>=st[l];j--)is(s.rk[j]);
		}
		while(r>a[i].r){
			dl(s.rk[r]);
			r--;
		}
		va=vv[r];
		for(int j=st[l];j<ed[l];j++)
			dl(s.rk[j]);
		for(int j=ed[l]-1;j>=a[i].l;j--)
			is(s.rk[j]);
		ans[a[i].i]=va;
		for(int j=a[i].l-1;j>=st[l];j--)is(s.rk[j]);
	}
	for(int i=1;i<=m;i++)
		cout<<ans[i]<<'\n';
}