#include<bits/stdc++.h>
#define fp(i,a,b) for(register int i=a,I=b+1;i<I;++i)
#define fd(i,a,b) for(register int i=a,I=b-1;i>I;--i)
#define go(u) for(register int i=fi[u],v=e[i].to;i;v=e[i=e[i].nx].to)
#define file(s) freopen(s".in","r",stdin),freopen(s".out","w",stdout)
template<class T>inline bool cmax(T&a,const T&b){return a<b?a=b,1:0;}
template<class T>inline bool cmin(T&a,const T&b){return a>b?a=b,1:0;}
using namespace std;
char sr[1<<21];int C=-1;
const int N=1e4+5,M=105,inf=1e9;
typedef int arr[N];
struct da{int l,c[26];}a[N];
int n,m,k,ans,pos,L=inf,R;arr pr,f;
char s[N][M];vector<int>len[M];
inline bool cmp(const da&a,const da&b){return a.l<b.l;}
void dfs(int u){
    if(!u)return;
    dfs(pr[u]);
    puts(s[u]+1);
}
inline bool chk(int u,int v){
    int p=0;
    fp(i,0,25){
        if(a[u].c[i]==a[v].c[i])continue;
        if(a[u].c[i]<a[v].c[i])return 0;
        if(a[u].c[i]>a[v].c[i]+1)return 0;
        p^=1;
    }return p;
}
int main(){
    #ifndef ONLINE_JUDGE
        file("s");
    #endif
    while(~scanf("%s",s[++n]+1)){
        a[n].l=strlen(s[n]+1);
        fp(i,1,a[n].l)++a[n].c[s[n][i]-'a'];
    }--n;
    fp(i,1,n)len[a[i].l].push_back(i),cmin(L,a[i].l),cmax(R,a[i].l);
    fp(l,L,R){
        for(int i:len[l])f[i]=1;
        if(!len[l-1].size())continue;
        for(int i:len[l]){
            for(int j:len[l-1]){
                if(chk(i,j)){
                    if(f[i]<f[j]+1)
                        f[i]=f[j]+1,pr[i]=j;
                }
            }
            if(f[i]>ans)ans=f[i],pos=i;
        }
    }
    printf("%d\n",ans);
    dfs(pos);
return 0;
}