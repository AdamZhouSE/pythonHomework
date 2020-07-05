#include <bits/stdc++.h>
using namespace std;
template<class t> inline t read(t &x){
	char c=getchar();bool f=0;x=0;
	while(!isdigit(c)) f|=c=='-',c=getchar();
	while(isdigit(c)) x=(x<<1)+(x<<3)+(c^48),c=getchar();
	if(f) x=-x;return x;
}
template<class t> inline void write(t x){
	if(x<0) putchar('-'),write(-x);
	else{if(x>9) write(x/10);putchar('0'+x%10);}
}

#define int long long

const int N=505;
bool v[N],g[N][N];
int cx[N],cy[N],n,ans;
vector<int> a,b;

bool dfs(int x){
	for(int y=0;y<b.size();y++) if(g[x][y]&&!v[y]){
		v[y]=1;
		if(cy[y]==-1||dfs(cy[y])){
			cx[x]=y;
			cy[y]=x;
			return 1;
		}
	}
	return 0;
}

signed main(){
	read(n);
	for(int i=1,x;i<=n;i++){
		read(x);
		if(x&1) a.push_back(x);
		else b.push_back(x);
	}
	for(int i=0;i<a.size();i++)
		for(int j=0;j<b.size();j++) if(__gcd(a[i],b[j])==1&&__gcd(a[i]+1,b[j]+1)==1)
			g[i][j]=1;
	for(int i=0;i<a.size();i++) cx[i]=-1;
	for(int i=0;i<b.size();i++) cy[i]=-1;
	for(int i=0;i<a.size();i++){
		for(int j=0;j<b.size();j++) v[j]=0;
		ans+=dfs(i);
	}
	write(n-ans);
}