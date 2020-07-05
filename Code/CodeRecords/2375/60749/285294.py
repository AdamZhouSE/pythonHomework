#include<cstdio>
#include<algorithm>
#define M 11000
#define N 2200
using namespace std;
inline int read(){
    int x=0;char ch=getchar();
    while (ch<'0'||ch>'9')ch=getchar();
    while (ch<='9'&&ch>='0'){x=x*10+ch-'0';ch=getchar();}
    return x;
}
struct node{
    int x,y,z;
}data[M];int fa[N],n,m;
inline bool cmp(node a,node b){return a.z<b.z;}
inline int find(int x){return fa[x]==x?x:fa[x]=find(fa[x]);}
int main(){
    freopen("1547.in","r",stdin);
    n=read();m=read();int ans=0;
    for (int i=1;i<=m;++i){
        int x=read(),y=read(),z=read();
        data[i].x=x;data[i].y=y;data[i].z=z;
    }
    sort(data+1,data+m+1,cmp);int cnt=0;for (int i=1;i<=n;++i) fa[i]=i;
    for (int i=1;i<=m;++i){
        int x=find(data[i].x),y=find(data[i].y);
        if (x!=y){
            ans=max(ans,data[i].z);
            fa[x]=y;if (++cnt==n-1) break;
        }
    }
    printf("%d",ans);
    return 0;
}

