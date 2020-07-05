#include<cstdio>
#include<cstring>
#include<algorithm>
#define N 100010
using namespace std;
int n,x,y,a[N],b[N],ls[N],rs[N],f[N],t,ans;
void dfs(int x){
	if(ls[x]) dfs(ls[x]);
	b[++b[0]]=x;
	if(rs[x]) dfs(rs[x]);
}
void add(int x){
	if(x>=f[t]||!t){
		f[++t]=x;
		return;
	}
	int l=1,r=t,mid,k=0;
	while(l<=r){
		mid=(l+r)>>1;
		if(x>=f[mid]) l=mid+1;
		else r=mid-1;
	}
	f[l]=x;
}
int main(){
	scanf("%d",&n);
	for(int i=1;i<=n;i++) scanf("%d",&a[i]);
	for(int i=2;i<=n;i++){
		scanf("%d%d",&x,&y);
		if(!y) ls[x]=i;
		else rs[x]=i;
	}
	dfs(1);
	for(int i=1;i<=n;i++) add(a[b[i]]-i);
	printf("%d\n",n-t);
	return 0;
}