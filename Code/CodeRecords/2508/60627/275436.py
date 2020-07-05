#include<cstdio>
#include<iostream>
using namespace std;
const int maxn = 1007;
inline int read() {
    int x=0,f=1;
    char c=getchar() ;
    while(c<'0'||c>'9') {
        if(c=='-')f=-1;
        c=getchar();
    }
    while(c>='0'&&c<='9')
        x=x*10+c-'0',c=getchar();
    return x*f;
}
struct node {
    int v,next,w;
}edge[maxn];
int head[maxn],num=0;
inline void add_edge(int u,int v,int w) {
    edge[++num].v=v;edge[num].w=w;edge[num].next=head[u];head[u]=num;
}
int n,k;
int dp[maxn][maxn]; 
void dfs(int x,int f) {
    for(int i=head[x];i;i=edge[i].next) {
        int v=edge[i].v;
        //dp[v][1]=edge[i].w;
        if(v==f)continue;
        dfs(v,x);
        for(int j=k;j>=1;j--) 
            for(int p=0;p<j;p++) 
                dp[x][j]=max(dp[x][j],dp[v][p]+dp[x][j-p-1]+edge[i].w); //从子树v中选取p条
                //再从其他子树中选取j-p-1条，加上连接v与x的苹果数. 
    }
}
int main () { 
    n=read(),k=read();
    for(int a,b,c,i=1;i<n;++i) {
        a=read(),b=read(),c=read();
        add_edge(a,b,c);
        add_edge(b,a,c);
    }
    dfs(1,0);
    printf("%d\n",dp[1][k]);
    return 0;
}