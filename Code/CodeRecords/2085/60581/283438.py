#include<iostream>
#include<cstring>
#include<cmath>
#include<queue>
#include<cstdio>
#include<algorithm>
#define LL long long
#define INF 0x3f3f3f3f
using namespace std;
const int N=4*2e5+100;
const int M=4e4+100;
struct Edge {
   int u,v,w;
} err[M];
int pre[N],ine[N];//ine:最短弧集合
int vis[N],id[N];
LL zhuliu(int n,int m,int root) {
   LL ans=0;
   while(1) {
      for(int i=1; i<=n; ++i) ine[i]=INF;  // 初始化
      for(int i=1; i<=m; ++i) {
         int u=err[i].u,v=err[i].v;
         if(u!=v&&err[i].w<ine[v])  // 遍历所有边，对每个点找到最小的入边
            ine[v]=err[i].w,pre[v]=u;
      }
      for(int i=1; i<=n; ++i)  // 判定无解
         if(i!=root&&ine[i]==INF) return -1;
      int cnt=0;
      for(int i=1; i<=n; ++i) vis[i]=id[i]=0;
      for(int i=1; i<=n; ++i) {
         if(i==root) continue;
         ans+=ine[i];
         int v=i;
         while(vis[v]!=i&&!id[v]&&v!=root) { // 找环
            vis[v]=i;
            v=pre[v];
         }
         if(!id[v]&&v!=root) {
            id[v]=++cnt;  // 把环上的店标记为同一点
            for(int u=pre[v]; u!=v; u=pre[u])
               id[u]=cnt;
         }
      }
      if(cnt==0) break; // 无环，得到解
      for(int i=1; i<=n; ++i)
         if(!id[i]) id[i]=++cnt;
      for(int i=1; i<=m; ++i) {
         int u=err[i].u,v=err[i].v;
         err[i].u=id[u],err[i].v=id[v];
         if(id[u]!=id[v]) err[i].w-=ine[v]; // 修改边权
      }
      root=id[root];
      n=cnt;
   }
   return ans;
}
int main() {
//   freopen("input.txt","r",stdin);
//   freopen("output.txt","w",stdout);
   int n,m,r;
   while(cin>>n>>m>>r) {
      for(int i=1; i<=m; i++) {
         cin>>err[i].u>>err[i].v>>err[i].w;
      }
      LL ans=zhuliu(n,m,r);
      cout<<ans;
 
   }
   return 0;
 
}