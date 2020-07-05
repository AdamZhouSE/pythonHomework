#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;
const int N=10005,M=20005;
struct edge{
    int u,v,c1,c2,x;
}a[M],b[M];
int n,m,k,f[N];
bool vis[M];
int findf(int u){
    return f[u]=f[u]==u?u:findf(f[u]);
}
bool cmp1(edge a,edge b){
    return a.c1<b.c1;
}
bool cmp2(edge a,edge b){
    return a.c2<b.c2;
}
int main(){
    int i,sum,ans;
    scanf("%d%d%d",&n,&k,&m);
    --m;
    for(i=1;i<=n;i++){
        f[i]=i;
    }
    for(i=1;i<=m;i++){
        scanf("%d%d%d%d",&a[i].u,&a[i].v,&a[i].c1,&a[i].c2);
        a[i].x=i;
        b[i]=a[i];
    }
    sort(a+1,a+m+1,cmp1);
    sort(b+1,b+m+1,cmp2);
    for(i=1,sum=0;i<=m;i++){
        int x=findf(a[i].u),y=findf(a[i].v);
        if(x!=y){
            f[x]=y;
            sum++;
            vis[a[i].x]=1;
        }
        if(sum==k){
            ans=a[i].c1;
            break;
        }
    }
    for(i=1;i<=m;i++){
        if(vis[b[i].x]){
            continue;
        }
        int x=findf(b[i].u),y=findf(b[i].v);
        if(x!=y){
            f[x]=y;
            ans=max(ans,b[i].c2);
            sum++;
        }
        if(sum==n-1){
            break;
        }
    }
    printf("%d\n",ans);
    return 0;
}

