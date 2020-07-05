#include<bits/stdc++.h>
#define ui unsigned int
#define ll long long
#define db double
#define ld long double
#define ull unsigned long long
const int MAXN=100000+10,MAXM=100000+10;
int n,m,fa[MAXN<<1],len[MAXN<<1],ch[MAXN<<1][2],ans[MAXM],las=1,tot=1,ps[MAXN];
char s[MAXN];
struct node{
    int l,r,id;
    inline bool operator < (const node &A) const {
        return r<A.r||(r==A.r&&l<A.l);
    };
};
node query[MAXM];
template<typename T> inline void read(T &x)
{
    T data=0,w=1;
    char ch=0;
    while(ch!='-'&&(ch<'0'||ch>'9'))ch=getchar();
    if(ch=='-')w=-1,ch=getchar();
    while(ch>='0'&&ch<='9')data=((T)data<<3)+((T)data<<1)+(ch^'0'),ch=getchar();
    x=data*w;
}
template<typename T> inline void write(T x,char ch='\0')
{
    if(x<0)putchar('-'),x=-x;
    if(x>9)write(x/10);
    putchar(x%10+'0');
    if(ch!='\0')putchar(ch);
}
template<typename T> inline void chkmin(T &x,T y){x=(y<x?y:x);}
template<typename T> inline void chkmax(T &x,T y){x=(y>x?y:x);}
template<typename T> inline T min(T x,T y){return x<y?x:y;}
template<typename T> inline T max(T x,T y){return x>y?x:y;}
#define Mid ((l+r)>>1)
#define ls rt<<1
#define rs rt<<1|1
#define lson ls,l,Mid
#define rson rs,Mid+1,r
struct Segment_Tree{
    int Mx[MAXN<<2];
    inline void PushUp(int rt)
    {
        Mx[rt]=max(Mx[ls],Mx[rs]);
    }
    inline void Update(int rt,int l,int r,int ps,int k)
    {
        if(l==r&&r==ps)chkmax(Mx[rt],k);
        else
        {
            if(ps<=Mid)Update(lson,ps,k);
            else Update(rson,ps,k);
            PushUp(rt);
        }
    }
    inline int Query(int rt,int l,int r,int L,int R)
    {
        if(L<=l&&r<=R)return Mx[rt];
        else
        {
            int res=0;
            if(L<=Mid)chkmax(res,Query(lson,L,R));
            if(R>Mid)chkmax(res,Query(rson,L,R));
            return res;
        }
    }
};
Segment_Tree sT;
#undef Mid
#undef ls
#undef rs
#undef lson
#undef rson
#define lc(x) ch[(x)][0]
#define rc(x) ch[(x)][1]
struct LinkCut_Tree{
    int ch[MAXN<<1][2],fa[MAXN<<1],stack[MAXN<<1],val[MAXN<<1],pd[MAXN<<1],cnt;
    inline bool nroot(int x)
    {
        return lc(fa[x])==x||rc(fa[x])==x;
    }
    inline void pushdown(int x)
    {
        if(pd[x])
        {
            if(lc(x))val[lc(x)]=pd[lc(x)]=pd[x];
            if(rc(x))val[rc(x)]=pd[rc(x)]=pd[x];
            pd[x]=0;
        }
    }
    inline void rotate(int x)
    {
        int f=fa[x],p=fa[f],c=(rc(f)==x);
        if(nroot(f))ch[p][rc(p)==f]=x;
        fa[ch[f][c]=ch[x][c^1]]=f;
        fa[ch[x][c^1]=f]=x;
        fa[x]=p;
    }
    inline void splay(int x)
    {
        cnt=0;
        stack[++cnt]=x;
        for(register int i=x;nroot(i);i=fa[i])stack[++cnt]=fa[i];
        while(cnt)pushdown(stack[cnt--]);
        for(register int y=fa[x];nroot(x);rotate(x),y=fa[x])
            if(nroot(y))rotate((lc(y)==x)==(lc(fa[y])==y)?y:x);
    }
    inline void access(int x)
    {
        for(register int y=0;x;x=fa[y=x])
        {
            splay(x);
            if(val[x])sT.Update(1,1,n,val[x],len[x]);
            rc(x)=y;
        }
    }
};
LinkCut_Tree lT;
#undef lc
#undef rc
inline void extend(int c,int i)
{
    int p=las,np=++tot;
    las=np;
    len[np]=len[p]+1;ps[i]=np;
    while(p&&!ch[p][c])ch[p][c]=np,p=fa[p];
    if(!p)fa[np]=1;
    else
    {
        int q=ch[p][c];
        if(len[q]==len[p]+1)fa[np]=q;
        else
        {
            int nq=++tot;
            fa[nq]=fa[q];
            memcpy(ch[nq],ch[q],sizeof(ch[nq]));
            len[nq]=len[p]+1;fa[q]=fa[np]=nq;
            while(p&&ch[p][c]==q)ch[p][c]=nq,p=fa[p];
        }
    }
}
int main()
{
    read(n);read(m);
    scanf("%s",s+1);
    for(register int i=1;i<=m;++i)
    {
        read(query[i].l),read(query[i].r);
        query[i].id=i;
    }
    std::sort(query+1,query+m+1);
    for(register int i=1,lt=strlen(s+1);i<=lt;++i)extend(s[i]-'0',i);
    for(register int i=1;i<=tot;++i)lT.fa[i]=fa[i];
    for(register int i=1,j=1;i<=n;++i)
    {
        lT.access(ps[i]);
        while(j<=m&&query[j].r==i)ans[query[j].id]=sT.Query(1,1,n,query[j].l,i),++j;
        lT.splay(ps[i]);lT.val[ps[i]]=lT.pd[ps[i]]=i;
    }
    for(register int i=1;i<=m;++i)write(ans[i],'\n');
    return 0;
}