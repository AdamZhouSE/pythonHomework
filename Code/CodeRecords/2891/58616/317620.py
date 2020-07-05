#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long ll;
inline void read(int &x){
	x=0;char ch;bool flag = false;
	while(ch=getchar(),ch<'!');if(ch == '-') ch=getchar(),flag = true;
	while(x=10*x+ch-'0',ch=getchar(),ch>'!');if(flag) x=-x;
}
inline int cat_max(const int &a,const int &b){return a>b ? a:b;}
inline int cat_min(const int &a,const int &b){return a<b ? a:b;}
const int maxn = 128;
int a[maxn];
int main(){
	int n;read(n);
	int maxx = 0;
	for(int i=1;i<=n;++i){
		read(a[i]);
		maxx = cat_max(maxx,a[i]);
	}
	int ans = 0;
	for(int i=1;i<=n;++i){
		ans += maxx - a[i];
	}printf("%d\n",ans);
	getchar();getchar();
	return 0;
}