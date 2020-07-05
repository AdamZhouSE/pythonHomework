#include<bits/stdc++.h>
#include<tr1/unordered_map>
#define R register
#define ll long long
#define ull unsigned long long
#define fp(i,a,b) for(R int i=(a),I=(b)+1;i<I;++i)
#define fd(i,a,b) for(R int i=(a),I=(b)-1;i>I;--i)
#define go(u) for(int i=head[u],v=e[i].v;i;i=e[i].nx,v=e[i].v)
using namespace std;
using namespace std::tr1;
char buf[1<<21],*p1=buf,*p2=buf;
inline char getc(){return p1==p2&&(p2=(p1=buf)+fread(buf,1,1<<21,stdin),p1==p2)?EOF:*p1++;}
int read(){
    R int res,f=1;R char ch;
    while((ch=getc())>'9'||ch<'0')(ch=='-')&&(f=-1);
    for(res=ch-'0';(ch=getc())>='0'&&ch<='9';res=res*10+ch-'0');
    return res*f;
}
int read(char *s){
    R int len=0;R char ch;while(((ch=getc())>'z'||ch<'a'));
    for(s[++len]=ch;(ch=getc())>='a'&&ch<='z';s[++len]=ch);
    return s[len+1]='\0',len;
}
char sr[1<<21],z[20];int C=-1,Z=0;
inline void Ot(){fwrite(sr,1,C+1,stdout),C=-1;}
void print(R ll x){
    if(C>1<<20)Ot();if(x<0)sr[++C]='-',x=-x;
    while(z[++Z]=x%10+48,x/=10);
    while(sr[++C]=z[Z],--Z);sr[++C]='\n';
}
const int N=2e5+5,M=N*20+5,Base=131;
struct node{
    int s,t,l,r,id,L;
    inline void init(R int Id){s=read(),t=read(),l=read(),r=read(),id=Id,L=r-l+1;}
    inline bool operator <(const node &b)const{return L<b.L;}
}q[N];
char s[N],t[N];
int ch[N][26],fa[N],l[N],rt[N],f[N][21],F[N][21],G[N][21],lc[M],rc[M],sz[M];ll ans[N];
int c[N],a[N],id[N],mx[N],poi[N],Log[N],cl[N],zz[N];ull bin[N],h[N];
int las=1,cnt=1,tot,n,k,T;unordered_map<ull,int>mp;
inline ull gh(R int l,R int r){return h[r]-h[l-1]*bin[r-l+1];}
void ins(int c){
    int p=las,np=las=++cnt;l[np]=l[p]+1;
    for(;p&&!ch[p][c];p=fa[p])ch[p][c]=np;
    if(!p)fa[np]=1;
    else{
        int q=ch[p][c];
        if(l[q]==l[p]+1)fa[np]=q;
        else{
            int nq=++cnt;l[nq]=l[p]+1;
            memcpy(ch[nq],ch[q],4*26);
            fa[nq]=fa[q],fa[q]=fa[np]=nq;
            for(;p&&ch[p][c]==q;p=fa[p])ch[p][c]=nq;
        }
    }
}
void upd(int &p,int l,int r,int x){
    if(!p)p=++tot;++sz[p];if(l==r)return;
    int mid=(l+r)>>1;
    x<=mid?upd(lc[p],l,mid,x):upd(rc[p],mid+1,r,x);
}
int merge(int x,int y){
    if(!x||!y)return x|y;
    int p=++tot;
    lc[p]=merge(lc[x],lc[y]),rc[p]=merge(rc[x],rc[y]);
    sz[p]=sz[lc[p]]+sz[rc[p]];return p;
}
int find(int p,int l,int r){
    if(l==r)return l;
    int mid=(l+r)>>1;
    return sz[lc[p]]?find(lc[p],l,mid):find(rc[p],mid+1,r);
}
int query(int p,int l,int r,int ql,int qr){
    if(!sz[p])return -1;if(ql<=l&&qr>=r)return find(p,l,r);
    int mid=(l+r)>>1,res=-1;
    if(ql<=mid&&(res=query(lc[p],l,mid,ql,qr))!=-1)return res;
    if(qr>mid&&(res=query(rc[p],mid+1,r,ql,qr))!=-1)return res;
    return -1;
}
void solve_min(int p,int l,int r,int L,int id){
    ll c=0,d=0;int x=query(rt[p],1,n,l,r);
    if(x==-1)return ans[id]=0,void();
    fd(i,zz[x],0)if(F[x][i]&&F[x][i]<=r)c+=(1<<i),d+=G[x][i],x=F[x][i];
    ++c,d+=x,ans[id]=c*k-d+(L-1)*c;
}
void solve_max(int p,int l,int r,int L,int id){
    ll c=0,d=0;int x;
    while(l<=r){
        x=query(rt[p],1,n,l,r);
        if(x==-1)break;
        ++c,d+=x,l=x+L;
    }
    ans[id]=c*k-d+(L-1)*c;
}
void init(){
    n=read(),k=read(),read(s),read(t);
    fp(i,1,n)ins(s[i]-'a'),upd(rt[las],1,n,i);
    fp(i,1,cnt)f[i][0]=fa[i],++c[l[i]];
    for(R int j=1;(1<<j)<=cnt;++j)fp(i,1,cnt)f[i][j]=f[f[i][j-1]][j-1];
    fp(i,1,cnt)c[i]+=c[i-1];
    fd(i,cnt,1)id[c[l[i]]--]=i;
    for(R int i=cnt,p=id[i];i>1;--i,p=id[i])
        rt[fa[p]]=merge(rt[fa[p]],rt[p]);
    for(R int i=1,p=1,now=0;i<=n;++i){
        R int c=t[i]-'a';
        if(ch[p][c])p=ch[p][c],++now;
        else{
            for(;p&&!ch[p][c];p=fa[p]);
            p?(now=l[p]+1,p=ch[p][c]):(p=1,now=0);
        }
        mx[i]=now,poi[i]=p;
    }
    bin[0]=1,Log[0]=-1;
    fp(i,1,n)bin[i]=bin[i-1]*Base,h[i]=h[i-1]*Base+s[i]-'a'+1,Log[i]=Log[i>>1]+1;
}
void solve(){
    T=read();fp(i,1,T)q[i].init(i);
    sort(q+1,q+1+T);
    int pos=1,s,t,l,r,id,p,L;
    for(R int L=1;L<=50;++L)if(q[pos].L==L){
        fd(i,n,L){
            R ull tmp=gh(i-L+1,i);
            if(mp.count(tmp)){
                R int x=mp[tmp],sz=Log[cl[x]+1];
                zz[i]=sz,F[i][0]=x,G[i][0]=i,cl[i]=cl[x]+1;
                fp(j,1,sz){
                    x=F[i][j-1];
                    F[i][j]=F[x][j-1],G[i][j]=G[i][j-1]+G[x][j-1];
                }
            }else cl[i]=0;
            if(i+L-1<=n)mp[gh(i,i+L-1)]=i+L-1;
        }
        unordered_map<ull,int>().swap(mp);
        for(;pos<=T&&q[pos].L==L;++pos){
            s=q[pos].s,t=q[pos].t,l=q[pos].l,r=q[pos].r,id=q[pos].id;
            if(mx[r]<L){ans[id]=0;continue;}
            p=poi[r];
            fd(j,Log[::l[p]],0)if(::l[f[p][j]]>=L)p=f[p][j];
            solve_min(p,s+L-1,t,L,id);
        }
        fd(i,n,L)fp(j,0,zz[i])F[i][j]=G[i][j]=0;
    }
    for(;pos<=T;++pos){
        s=q[pos].s,t=q[pos].t,l=q[pos].l,r=q[pos].r,id=q[pos].id,L=r-l+1;
        if(mx[r]<L){ans[id]=0;continue;}
        p=poi[r];
        fd(j,Log[::l[p]],0)if(::l[f[p][j]]>=L)p=f[p][j];
        solve_max(p,s+L-1,t,L,id);
    }
    fp(i,1,T)print(ans[i]);
}
int main(){
//  freopen("testdata.in","r",stdin);
    init(),solve();
    return Ot(),0;
}