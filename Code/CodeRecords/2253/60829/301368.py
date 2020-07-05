#include<cstdio>
#include<algorithm>
using namespace std;
const int INF=2147483647;
const int N=4e6+5;
inline int read(){
    int X=0,w=0;char ch=0;
    while(ch<'0'||ch>'9'){w|=ch=='-';ch=getchar();}
    while(ch>='0'&&ch<='9')X=(X<<3)+(X<<1)+(ch^48),ch=getchar();
    return w?-X:X;
}
int s[N],maxn,rt[N],sz;
int fa[N],tr[N][2],key[N],size[N],cnt[N];
inline bool get(int x){
    return tr[fa[x]][1]==x;
}
inline void clear(int x){
    fa[x]=tr[x][0]=tr[x][1]=key[x]=cnt[x]=size[x]=0;
}
inline void splay_upd(int x){
    if(!x)return;
    size[x]=cnt[x];  
    if(tr[x][0])size[x]+=size[tr[x][0]];  
    if(tr[x][1])size[x]+=size[tr[x][1]];
}
inline void rotate(int x){
    int y=fa[x],z=fa[y],which=get(x);
    tr[y][which]=tr[x][which^1];fa[tr[y][which]]=y;  
    fa[y]=x;tr[x][which^1]=y;fa[x]=z;
    if(z)tr[z][tr[z][1]==y]=x;
    splay_upd(y);splay_upd(x);
}
inline void splay(int i,int x){
    int f=fa[x];
    while(f){
        if(fa[f])rotate(get(x)==get(f)?f:x);
        rotate(x);f=fa[x];
    }
    rt[i]=x;
}
inline void splay_ins(int i,int v){
    if(!rt[i]){
        rt[i]=++sz;
        fa[sz]=tr[sz][0]=tr[sz][1]=0;
        size[sz]=cnt[sz]=1;key[sz]=v;
        return;
    }
    int now=rt[i],f=0;
    while(233){
        if(key[now]==v){
            cnt[now]++;splay_upd(f);splay(i,now);
            return;
        }
        f=now;now=tr[now][key[now]<v];
        if(!now){
            ++sz;
            fa[sz]=f;tr[sz][0]=tr[sz][1]=0;
                size[sz]=cnt[sz]=1;key[sz]=v;
            tr[f][key[f]<v]=sz;
            splay_upd(f);splay(i,sz);
            return;
        }
    }
}
inline int splay_find(int i,int v){//查询比v小的数的个数 
    int ans=0,now=rt[i];
    while(233){
        if(!now)return ans;
        if(v<key[now])now=tr[now][0];
        else{
            ans+=(tr[now][0]?size[tr[now][0]]:0);
            if(v==key[now]){
                splay(i,now);
                return ans;
            }
            ans+=cnt[now];
            now=tr[now][1];
        }
    }
}
inline int splay_pre(int i){
    int now=tr[rt[i]][0];
    while(tr[now][1])now=tr[now][1];
    return now;
}
inline int splay_nxt(int i){
    int now=tr[rt[i]][1];
    while(tr[now][0])now=tr[now][0];
    return now;
}
inline void splay_del(int i,int x){
    splay_find(i,x);
    if(cnt[rt[i]]>1){
        cnt[rt[i]]--;return;
    }
    if(!tr[rt[i]][0]&&!tr[rt[i]][1]){
        clear(rt[i]);rt[i]=0;return;
    }
    if(!tr[rt[i]][0]){  
        int oldroot=rt[i];rt[i]=tr[rt[i]][1];fa[rt[i]]=0;clear(oldroot);return;
    }
    else if(!tr[rt[i]][1]){  
        int oldroot=rt[i];rt[i]=tr[rt[i]][0];fa[rt[i]]=0;clear(oldroot);return;
    }
    int leftbig=splay_pre(i),oldroot=rt[i];  
    splay(i,leftbig);
    fa[tr[oldroot][1]]=rt[i];
    tr[rt[i]][1]=tr[oldroot][1];
    clear(oldroot);
    splay_upd(rt[i]);
}
inline void seg_mdy(int a,int l,int r,int x,int v){
    splay_del(a,s[x]);splay_ins(a,v);
    if(l==r)return;
    int mid=(l+r)>>1;
    if(x<=mid)seg_mdy(a<<1,l,mid,x,v);
    else seg_mdy(a<<1|1,mid+1,r,x,v);
}
inline int seg_find(int a,int l,int r,int l1,int r1,int v){
    if(r<l1||r1<l)return 0;
    if(l1<=l&&r<=r1)return splay_find(a,v);
    int mid=(l+r)>>1;
    return seg_find(a<<1,l,mid,l1,r1,v)+seg_find(a<<1|1,mid+1,r,l1,r1,v);
}
inline int seg_pre(int a,int l,int r,int l1,int r1,int v){
    if(r<l1||r1<l)return -INF;
    if(l1<=l&&r<=r1){
        splay_ins(a,v);
        int tmp=splay_pre(a);
        splay_del(a,v);
        return !tmp?-INF:key[tmp];
    }
    int mid=(l+r)>>1;
    return max(seg_pre(a<<1,l,mid,l1,r1,v),seg_pre(a<<1|1,mid+1,r,l1,r1,v));
}
inline int seg_nxt(int a,int l,int r,int l1,int r1,int v){
    if(r<l1||r1<l)return INF;
    if(l1<=l&&r<=r1){
        splay_ins(a,v);
        int tmp=splay_nxt(a);
        splay_del(a,v);
        return !tmp?INF:key[tmp];
    }
    int mid=(l+r)>>1;
    return min(seg_nxt(a<<1,l,mid,l1,r1,v),seg_nxt(a<<1|1,mid+1,r,l1,r1,v));
}
inline void seg_build(int a,int l,int r){
    for(int i=l;i<=r;i++)splay_ins(a,s[i]);
    if(l==r)return;
    int mid=(l+r)>>1;
    seg_build(a<<1,l,mid);seg_build(a<<1|1,mid+1,r);
}
int main(){
    int n=read(),m=read();
    for(int i=1;i<=n;++i){
        s[i]=read(),maxn=max(maxn,s[i]);
    }
    seg_build(1,1,n);
    for(int i=1;i<=m;++i){
        int op=read();
        if(op==1){
            int l=read(),r=read(),k=read();
            printf("%d\n",seg_find(1,1,n,l,r,k)+1);
        }
        if(op==2){
            int l=read(),r=read(),k=read();
            int l1=0,r1=maxn+1;
            while(l1<r1){
                int mid=(l1+r1)>>1;
                int rk=seg_find(1,1,n,l,r,mid);
                if(rk<k)l1=mid+1;
                else r1=mid;
            }
            printf("%d\n",l1-1);
        }
        if(op==3){
            int pos=read(),k=read();
            seg_mdy(1,1,n,pos,k);
            s[pos]=k;maxn=max(maxn,s[pos]);
        }
        if(op==4){
            int l=read(),r=read(),k=read();
            printf("%d\n",seg_pre(1,1,n,l,r,k)); 
        }
        if(op==5){
            int l=read(),r=read(),k=read();
            printf("%d\n",seg_nxt(1,1,n,l,r,k)); 
        }
    }
    return 0;
}