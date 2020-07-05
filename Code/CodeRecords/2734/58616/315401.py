#include<map>
#include<cmath>
#include<stack>
#include<queue>
#include<cstdio>
#include<cctype>
#include<vector>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;
const int N=2e6+5;
inline int read(){
    int X=0,w=0;char ch=0;
    while(!isdigit(ch)){w|=ch=='-';ch=getchar();}
    while(isdigit(ch))X=(X<<3)+(X<<1)+(ch^48),ch=getchar();
    return w?-X:X;
}
struct data{
    int l,r,id;
}d[N];
int n,m,c,b[N],tr[N],ans[N],lst[N],nxt[N];
bool vis[N];
inline bool cmp(data a,data b){
    return a.l<b.l;
}
inline int lowbit(int t){return t&-t;}
inline void add(int x,int y){
    if(!x)return;
    for(int i=x;i<=n;i+=lowbit(i))tr[i]+=y;
}
inline int qry(int x){
    int res=0;
    for(int i=x;i;i-=lowbit(i))res+=tr[i];
    return res;
}
int main(){
    n=read(),c=read(),m=read();
    for(int i=1;i<=n;i++){
        b[i]=read();nxt[lst[b[i]]]=i;
        if(lst[b[i]]&&!vis[b[i]])vis[b[i]]=1,add(i,1);
        lst[b[i]]=i;
    }
    nxt[0]=0;
    for(int i=1;i<=m;i++){
        d[i].l=read(),d[i].r=read();
        d[i].id=i;
    }
    sort(d+1,d+m+1,cmp);
    for(int i=1,j=1;i<=n;i++){
        add(nxt[i-1],-1);add(nxt[nxt[i-1]],1);
        while(d[j].l==i){
            ans[d[j].id]=qry(d[j].r);
            j++;
        }
    }
    for(int i=1;i<=m;i++)printf("%d\n",ans[i]);
    return 0;
}