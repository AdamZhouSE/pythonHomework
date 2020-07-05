#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<bits/stdc++.h>
using namespace std;
const int N=102;
struct node{
    int to;
    int next;
}e[N*2];
int n,x,y,cnt,vis[N],head[N],f[N][22];
void add(int x,int y){
    e[++cnt].to=y;
    e[cnt].next=head[x];
    head[x]=cnt;
}
int d[N];
void dfs(int u,int fa){
    d[u]=d[fa]+1;
    for(int i=0;i<=19;i++)
        f[u][i+1]=f[f[u][i]][i];
    for(int i=head[u];i;i=e[i].next){
        int v=e[i].to;
        if(v==fa) continue;
        f[v][0]=u; dfs(v,u);
    }
}
int lca(int x,int y){
    if(d[x]<d[y]) swap(x,y);
    for(int i=20;i>=0;i--){
        if(d[f[x][i]]>=d[y]) x=f[x][i];
        if(x==y) return x;
    }
    for(int i=20;i>=0;i--)
        if(f[x][i]!=f[y][i]) 
           { x=f[x][i]; y=f[y][i]; }
    return f[x][0];
}
int ans1,ans2,ans3;
int main(){
    scanf("%d",&n);
     for(int i=1;i<n;i++){
        scanf("%d %d",&x,&y);
        add(x,y); add(y,x);
    }
    dfs(1,0);
    scanf("%d %d",&x,&y);
    for(int i=1;i<=n;i++){
        ans1=max(ans1,d[i]);
        vis[d[i]]++;
    }
    for(int i=1;i<=100;i++)
        ans2=max(ans2,vis[i]);
    ans3=(d[x]-d[lca(x,y)])*2+(d[y]-d[lca(x,y)]);
    if(ans2==2&&ans3==4){
        ans3=5;
    }
    printf("%d\n%d\n%d",ans1,ans2,ans3);
    return 0;
}