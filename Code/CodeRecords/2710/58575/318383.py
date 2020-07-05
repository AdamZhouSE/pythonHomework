#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N=200000+7,INF=0x3f7f3f7f;
inline int _min(int a,int b){return a<b?a:b;}
inline int read(){
    char c;int f=0,x=0;while(!isdigit(c=getchar()))if(c==45)f=1;
    while(isdigit(c))x=(x<<1)+(x<<3)+(c^48),c=getchar();return f?-x:x;
}
int minv[N<<2];
char s[3];
int n,q,x,k,ans,qr,ql;
#define l i<<1
#define r i<<1|1
void Update(int i,int L,int R){
    if(L==R){minv[i]=k;return;}
    int mid=L+R>>1;x<=mid?Update(l,L,mid):Update(r,mid+1,R);
    minv[i]=_min(minv[l],minv[r]);
}
int Find(int i,int L,int R){
    if(minv[i]>k)return INF;
    else if(L==R) return L; 
    int mid=L+R>>1;return minv[l]<=k?Find(l,L,mid):Find(r,mid+1,R);
}
void Query(int i,int L,int R){
    if(ql<=L&&qr>=R){ans=Find(i,L,R);return;}
    int mid=L+R>>1;
    if(ql<=mid){Query(l,L,mid);if(ans!=INF)return;}
    if(qr>mid)Query(r,mid+1,R);
}
#undef l
#undef r
int main(){
    qr=n=read(),q=read();memset(minv,INF,sizeof minv);
    while(q--){
        scanf("%s",s);
        if(s[0]=='M')k=read(),x=read(),Update(1,1,n);
        else k=read(),ql=read(),ans=INF,Query(1,1,n),printf("%d\n",ans==INF?-1:ans);
    }
    return 0;
}