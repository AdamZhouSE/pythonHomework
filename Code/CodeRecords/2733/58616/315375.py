#include<cstdio>
#include<algorithm>
#include<time.h>
#include<iostream>
#include<cstdio>
#include<queue>
#include<string.h>
#include<math.h>
#include<vector>
#include<algorithm>
#include<stdio.h>
#include<map>
using namespace std;
#define maxn 100005
const int MOD=1000000007;
int val[maxn],L[maxn],R[maxn],tot,a[maxn],t[maxn],vis[maxn];
vector<int>G[maxn];
int root[maxn],sz;
double ans[maxn];
struct node{
    int l,r,w;
}T[maxn*30];
 
void dfs(int u){
    vis[u]=1;
    L[u]=++tot;
    t[tot]=val[u],a[tot]=val[u];
    for(int i=0;i<G[u].size();i++){
        int v=G[u][i];
        if(vis[v]==1)
            continue;
        dfs(v);
    }
    R[u]=tot;
}
 
void update(int &i,int l,int r,int num){
    T[++sz]=T[i],i=sz;
    T[i].w++;
    if(l==r)
        return ;
    int mid=(l+r)>>1;
    if(num<=mid)
        update(T[i].l,l,mid,num);
    else
        update(T[i].r,mid+1,r,num);
}
 
int query(int x,int y,int l,int r,int k){
    if(l==r)
        return l;
    int mid=(l+r)>>1;
    int num=T[T[y].l].w-T[T[x].l].w;
    if(num>=k)
        return query(T[x].l,T[y].l,l,mid,k);
    else
        return query(T[x].r,T[y].r,mid+1,r,k-num);
}
 
int main(){
    int _,n,m,u,v,q;
    scanf("%d",&_);
    while(_--){
        scanf("%d%d",&n,&q);
        memset(vis,0,sizeof(vis));
        for(int i=1;i<=n;i++){
            scanf("%d",&val[i]);
            G[i].clear();
        }
        for(int i=1;i<n;i++){
            scanf("%d%d",&u,&v);
            G[u].push_back(v);
            G[v].push_back(u);
        }
        tot=0;
        dfs(1);
        sort(t+1,t+n+1);
        int m=unique(t+1,t+n+1)-t-1;
        root[0]=0,sz=0;
        for(int i=1;i<=n;i++){  //有序
            root[i]=root[i-1];
            int num=lower_bound(t+1,t+m+1,a[i])-t;
            update(root[i],1,n,num);
        }
        for(int i=1;i<=n;i++){
            if((R[i]-L[i])%2==1){
                int num1=query(root[L[i]-1],root[R[i]],1,n,(R[i]-L[i]+1)/2);
                int num2=query(root[L[i]-1],root[R[i]],1,n,(R[i]-L[i]+1)/2+1);
                ans[i]=1.0*(t[num1]+t[num2])/2;
            }
            else
                ans[i]=t[query(root[L[i]-1],root[R[i]],1,n,(R[i]-L[i])/2+1)];
        }
        double ANS=0;
        for(int i=1;i<=q;i++){
            scanf("%d",&u);
            ANS=fmod(ans[u]+ANS*10,1.0*MOD);
        }
        printf("%.1f\n",ANS);
    }
    return 0;
}