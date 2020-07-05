#include<cstdio>
#include<cctype>
#include<cstring>
#define ll long long
#include<algorithm>
using namespace std;
const int N=200020; 
inline char gc(){
    static char now[1<<16],*S,*T;
    if (T==S){T=(S=now)+fread(now,1,1<<16,stdin);if(T==S) return EOF;}
    return *S++;
}
int cnt=1,last=1,root=1,ch[N<<1][26],len[N<<1],fa[N<<1],size[N<<1];
int C[N],rk[N<<1],e[N<<1],sub[N<<1];ll ans;
inline void insert1(int x){static int p,np,q,nq;
    np=++cnt,p=last;len[np]=len[p]+1;
    for (;p&&!ch[p][x];p=fa[p]) ch[p][x]=np;
    if (!p) fa[np]=root;else{
        q=ch[p][x];if (len[p]+1==len[q]) fa[np]=q;else{
            nq=++cnt;len[nq]=len[p]+1;fa[nq]=fa[q];memcpy(ch[nq],ch[q],sizeof(ch[nq]));
            fa[q]=fa[np]=nq;for(;p&&ch[p][x]==q;p=fa[p]) ch[p][x]=nq;
        }
    }size[np]=1;last=np;
}
int main(){
//  freopen("bzoj4566.in","r",stdin);
    char c=gc();while(c<'a'||c>'z') c=gc();int le=0;
    while(c>='a'&&c<='z') insert1(c-'a'),c=gc(),++le;
    for (int i=1;i<=cnt;++i) ++C[len[i]];
    for (int i=1;i<=le;++i) C[i]+=C[i-1];
    for (int i=1;i<=cnt;++i) rk[C[len[i]]--]=i;
    for (int i=cnt;i;--i){
        static int x;x=rk[i];
        size[fa[x]]+=size[x];
    }c=gc();while(c<'a'||c>'z') c=gc();int p=1,l=0;
    while(c>='a'&&c<='z'){static int x;x=c-'a';
        if (ch[p][x]) {p=ch[p][x];++l;}else{
            for (;p&&!ch[p][x];p=fa[p]);
            if (!p) {p=1;l=0;}else l=len[p]+1,p=ch[p][x];
        }c=gc();ans+=(ll)(l-len[fa[p]])*size[p];++e[p];
    }
    for (int i=cnt;i>=2;--i){
        static int x;x=rk[i];
        sub[fa[x]]+=sub[x]+e[x];
    }
    for (int i=2;i<=cnt;++i){
        static int x;x=rk[i];
        ans+=(ll)sub[x]*size[x]*(len[x]-len[fa[x]]);
    }printf("%lld\n",ans);
    return 0;
}
————————————————
版权声明：本文为CSDN博主「elijahqi」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/elijahqi/article/details/79906912