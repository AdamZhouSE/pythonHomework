#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[500010],nxt[500010],p[500010],tot;
int dis[500010],dft[500010],root,cnt;
int x[500010],y[500010];
int d[500010],top;
int f[500010],size[500010],num[500010];
int n,m;
bool vis[500010];
 
inline int tmp(int a,int b)
{
	return a>b;
}
inline void add(int x,int y)
{
	tot++; a[tot]=y; nxt[tot]=p[x]; p[x]=tot;
}
 
void tarjan(int u)
{
	dis[u]=dft[u]=++cnt;
	d[++top]=u; 
	vis[u]=1;
	int v=p[u];
	while(v>=0)
	 {
	 	if(!dft[a[v]])
	 	 {
	 	 	tarjan(a[v]);
	 	 	dis[u]=min(dis[u],dis[a[v]]);
		  }
		 else
		  if(vis[a[v]]&&dis[u]>dft[a[v]]) dis[u]=dft[a[v]];
		v=nxt[v];
	 }
	int b;
	if(dis[u]==dft[u])
	 {
	 	++root;
	 	do{
	 		b=d[top--];
	 	    size[root]++;
	 		f[b]=root;
	 		vis[b]=0;
		 }while(u!=b);
	 }
	return; 
}
inline void slove()
{
	cnt=top=root=0;
	memset(dis,0,sizeof(dis));
	memset(dft,0,sizeof(dft));
	for(int i=1;i<=n;++i)
	 if(!dft[i]) tarjan(i);
	return;
}
inline void count()
{
    for(int i=1;i<=m;++i)
     if(f[x[i]]!=f[y[i]])
       num[f[x[i]]]++;
    return;
}
 
int main()
{
	int i,j;
	memset(p,-1,sizeof(p));
	memset(nxt,-1,sizeof(nxt));
	memset(num,0,sizeof(num));
	scanf("%d%d",&n,&m);
	for(i=1;i<=m;++i)
	  {
	  	scanf("%d%d",&x[i],&y[i]);
	  	add(x[i],y[i]);
 	  }//不知道为什么，如果每条边只存一遍，就会WA（重复的边也要存储） 
	slove();
	count();
	int ans=0;
	for(i=1;i<=root;++i)
	  if(!num[i])
	   {
	   	if(ans)
	     {printf("0\n"); return 0;}
	    ans=i;
	   }
	printf("%d\n",size[ans]);
	return 0;
}