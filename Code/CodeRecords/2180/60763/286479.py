//
// Created by Jostar on 2020/3/16.
//
#include<cstdio>
#include<iostream>
#include<queue>
#include<cstring>
#include<algorithm>
#include<cctype>
using namespace std;
typedef long long ll;
const int N=8e5+5;
struct tree{
    int a[26],fa,l;
}tr[N];
char s[N];
int tot,pos[N];
int a[N],w[N],len;
ll size[2][N];
inline int insert(int p,int c,int id){
    int np=tr[p].a[c];
    if(np&&tr[np].l==tr[p].l+1){
        size[id][np]++;
        return np;
    }
    np=++tot;tr[np].l=tr[p].l+1;
    for(;p&&!tr[p].a[c];p=tr[p].fa)tr[p].a[c]=np;
    if(!p)tr[np].fa=1;
    else{
        int q=tr[p].a[c];
        if(tr[p].l+1==tr[q].l)tr[np].fa=q;
        else{
            int nq=++tot;tr[nq].l=tr[p].l+1;
            memcpy(tr[nq].a,tr[q].a,sizeof(tr[q].a));
            tr[nq].fa=tr[q].fa;tr[q].fa=tr[np].fa=nq;
            for(;p&&tr[p].a[c]==q;p=tr[p].fa)tr[p].a[c]=nq;
        }
    }
    size[id][np]++;
    return np;
}
int main(){
    tot=1;pos[0]=1;
    cin>>s+1;
    int n=strlen(s+1);
    for(int i=1;i<=n;i++)pos[i]=insert(pos[i-1],s[i]-'a',0);
    cin>>s+1;
    len=n;n=strlen(s+1);len=max(len,n);
    for(int i=1;i<=n;i++)pos[i]=insert(pos[i-1],s[i]-'a',1);
    for(int i=1;i<=tot;i++)w[tr[i].l]++;
    for(int i=1;i<=len;i++)w[i]+=w[i-1];
    for(int i=1;i<=tot;i++)a[w[tr[i].l]--]=i;
    ll ans=0;
    for(int i=tot;i>1;i--){
        size[0][tr[a[i]].fa]+=size[0][a[i]];
        size[1][tr[a[i]].fa]+=size[1][a[i]];
        ans+=size[0][a[i]]*size[1][a[i]]*(tr[a[i]].l-tr[tr[a[i]].fa].l);
    }
    cout << ans;
//    printf("%lld\n",ans);
    return 0;
}