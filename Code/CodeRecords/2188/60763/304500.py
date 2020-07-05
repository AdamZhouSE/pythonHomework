#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<queue>
#include<unordered_map>
#define maxn 300005
#define ll long long
using namespace std;
struct node{int l1,r1,l2,r2,id;}Q[maxn];
bool operator <(node a,node b){return a.r2-a.l2<b.r2-b.l2;}
int n,K;
char A[maxn],B[maxn];
namespace SGT
{
    int ls[maxn*60],rs[maxn*60],rt[maxn*60],rpos[maxn*60],tot;
    void ins(int &p,int l,int r,int x)
    {
        if(!p) p=++tot;
        if(l==r) {rpos[p]=x;return;}
        int mid=(l+r)>>1;
        if(x<=mid) ins(ls[p],l,mid,x);
        else ins(rs[p],mid+1,r,x);
        rpos[p]=max(rpos[ls[p]],rpos[rs[p]]);
    }
    int Merge(int u,int v,int l,int r)
    {
        if((!u)||(!v)) return (u?u:v);
        else if(l==r)
        {
            rpos[++tot]=l;
            return tot;
        }
        int New=++tot,mid=(l+r)>>1;
        ls[New]=Merge(ls[u],ls[v],l,mid);
        rs[New]=Merge(rs[u],rs[v],mid+1,r);
        rpos[New]=max(rpos[ls[New]],rpos[rs[New]]);
        return New;
    }
    int Query(int p,int l,int r,int x)
    {
        if(l==r) return l;
        int mid=(l+r)>>1;
        if(rpos[ls[p]]>=x) return Query(ls[p],l,mid,x);
        else return Query(rs[p],mid+1,r,x); 
    }
}
namespace SAM
{
    int mx[maxn],par[maxn],rt=1,tot=1,last=rt;
    int son[maxn][26],pos[maxn],buc[maxn],td[maxn],id[maxn];
    int Jump[22][maxn],enpos[maxn],enlen[maxn];
    int push(int x)
    {
        mx[++tot]=x;
        return tot;
    }
    void extend(int t)
    {
        int np,nq,p,q;
        np=push(mx[last]+1);
        for(p=last;p&&!son[p][t];p=par[p]) son[p][t]=np;
        if(!p) par[np]=rt;
        else
        {
            q=son[p][t];
            if(mx[q]==mx[p]+1) par[np]=q;
            else
            {
                nq=push(mx[p]+1),id[nq]=id[np];
                memcpy(son[nq],son[q],sizeof(son[q]));
                par[nq]=par[q],par[q]=par[np]=nq;
                for(;son[p][t]==q;p=par[p]) son[p][t]=nq;
            }
        }
        last=np;
    }
    void TopSort()
    {
        for(int i=1;i<=tot;i++) buc[mx[i]]++;
        for(int i=1;i<=n;i++) buc[i]+=buc[i-1];
        for(int i=1;i<=tot;i++) td[buc[mx[i]]--]=i;
    }
    void GetSegTree()
    {
        TopSort();
        for(int i=2;i<=tot;i++) SGT::ins(SGT::rt[i],1,n,id[i]);
        for(int i=tot;i>1;i--)
        {
            int t=td[i];
            if(par[t]!=1)
                SGT::rt[par[t]]=SGT::Merge(SGT::rt[par[t]],SGT::rt[t],1,n);
        }
    }
    int Run(int pos,int len)
    {
        int now=enpos[pos];
        if(enlen[pos]<len) return 0;
        for(int i=20;i>=0;i--)
            if(Jump[i][now]&&mx[Jump[i][now]]>=len)
                now=Jump[i][now];
        return now;
    }
    void GetJump()
    {
        for(int i=1;i<=tot;i++)
            Jump[0][i]=par[i];
        for(int i=1;i<=20;i++)
            for(int j=1;j<=tot;j++)
                Jump[i][j]=Jump[i-1][Jump[i-1][j]];
        for(int i=1,now=1,nowlen=0;i<=n;i++)
        {
            if(son[now][B[i]-'a'])
                nowlen++,now=son[now][B[i]-'a'];
            else
            {
                while(now&&!son[now][B[i]-'a']) now=par[now];
                if(!now) nowlen=0,now=rt;
                else nowlen=mx[now]+1,now=son[now][B[i]-'a'];
            }
            enpos[i]=now,enlen[i]=nowlen;
        }
    }
    ll Solve(int l1,int r1,int l2,int r2)
    {
        int len=r2-l2+1;
        r1=min(r1,K+len-1);
        int p=Run(l2+len-1,len);
        if(!p) return 0;
        if(SGT::rpos[SGT::rt[p]]<l1+len-1) return 0;
        int st=SGT::Query(SGT::rt[p],1,n,l1+len-1),en=r1;
        if(st>en) return 0;
        ll ans=0;
        while(st<=en)
        {
            if(st-len+1>=K) break;
            ans+=K-(st-len+1);
            if(SGT::rpos[SGT::rt[p]]<st+len) break;
            st=SGT::Query(SGT::rt[p],1,n,st+len); 
        }
        return ans;
    }
}
namespace MI
{
    const int P=1000000007ll;
    int nxt[21][100005]; ll sum[21][maxn];
    ll Ha[maxn],pw[maxn];
    void GetHash()
    {
        pw[0]=1;
        for(int i=1;i<maxn;i++) pw[i]=pw[i-1]*P; 
        for(int i=1;i<=n;i++) Ha[i]=Ha[i-1]+A[i]*pw[i];
    }
    void GetNxt(int len)
    {
        unordered_map<ll,deque<int>> pre;
        memset(nxt,0,sizeof(nxt));
        for(int i=1;i<=n-len+1;i++)
        {
            ll now=Ha[i+len-1]-Ha[i-1];
            now*=pw[n-len-i+1];
            while(pre[now].front()<=i-len&&pre[now].size())
                nxt[0][pre[now].front()]=i,pre[now].pop_front();
            pre[now].push_back(i); 
            sum[0][i]=K-i;
        }
        for(int j=1;j<=20;j++)
            for(int i=1;i<=n-len+1;i++)
                nxt[j][i]=nxt[j-1][nxt[j-1][i]],sum[j][i]=sum[j-1][i]+sum[j-1][nxt[j-1][i]];
    }
    ll Solve(int l1,int r1,int l2,int r2)
    {
        int len=r2-l2+1;
        r1=min(r1,K+len-1);
        int p=SAM::Run(l2+len-1,len);
        if(!p) return 0;
        if(SGT::rpos[SGT::rt[p]]<l1+len-1) return 0;
        int st=SGT::Query(SGT::rt[p],1,n,l1+len-1)-len+1,en=r1-len+1;
        if(st>en) return 0;
        ll ans=0;
        for(int i=20;i>=0;i--)
            if(nxt[i][st]&&nxt[i][st]<=en)
                ans+=sum[i][st],st=nxt[i][st];
        ans+=sum[0][st];
        return ans;
    }
}
ll ans[maxn];
int main()
{
    scanf("%d%d",&n,&K);
    scanf("%s%s",A+1,B+1);
    for(int i=1;i<=n;i++)
        SAM::id[SAM::tot+1]=i,SAM::extend(A[i]-'a');
    SAM::GetSegTree(),SAM::GetJump();
    MI::GetHash();
    int T; scanf("%d",&T);
    for(int i=1;i<=T;i++)
        scanf("%d%d%d%d",&Q[i].l1,&Q[i].r1,&Q[i].l2,&Q[i].r2),Q[i].id=i;
    sort(Q+1,Q+T+1);
    for(int i=1;i<=T;i++)
    {
        if(Q[i].r2-Q[i].l2+1<=51)
        {
            if(Q[i].r2-Q[i].l2!=Q[i-1].r2-Q[i-1].l2||i==1)
                MI::GetNxt(Q[i].r2-Q[i].l2+1);
            ans[Q[i].id]=MI::Solve(Q[i].l1,Q[i].r1,Q[i].l2,Q[i].r2);
        }
        else ans[Q[i].id]=SAM::Solve(Q[i].l1,Q[i].r1,Q[i].l2,Q[i].r2);
    }
    for(int i=1;i<=T;i++) printf("%lld\n",ans[i]);
    return 0;
}