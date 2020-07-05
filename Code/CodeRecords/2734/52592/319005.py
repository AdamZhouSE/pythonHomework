#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
struct node
{
    int l,r,pos;
}t[2000010];
int last1[2000010],last2[2000010],c[2000010],a[2000010],ans[2000010];
int n,q,m;
inline bool cmp(node A,node B){
   return A.r<B.r;
}
inline void add(int x,int val){
    for(int i=x;i<=n;i+=(i&-i))c[i]+=val;
}
inline int query(int x){
    int ans=0;
    for(int i=x;i;i-=(i&-i))ans+=c[i];
    return ans;
}
int main(){
    scanf("%d%d%d",&n,&q,&m);
    for(int i=1;i<=n;++i)scanf("%d",&a[i]);
    for(int i=1;i<=m;++i){
       scanf("%d%d",&t[i].l,&t[i].r);
       t[i].pos=i;
    }
    sort(t+1,t+m+1,cmp);
    int j=1;
    for(int i=1;i<=m;++i){
        for(;j<=t[i].r;++j){
           if(!last1[a[j]])last1[a[j]]=j;
           else {
              if(!last2[a[j]]){
                add(last1[a[j]],1);
                last2[a[j]]=j;
              }else {
                 add(last2[a[j]],1);
                 add(last1[a[j]],-1);
                 last1[a[j]]=last2[a[j]];
                 last2[a[j]]=j;
              } 
           }
        }
        ans[t[i].pos]=query(t[i].r)-query(t[i].l-1);
    }
    for(int i=1;i<=m;++i)printf("%d\n",ans[i]);
    return 0;
}