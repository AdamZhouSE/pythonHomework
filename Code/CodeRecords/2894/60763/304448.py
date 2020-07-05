#include"cstdio"
#include"cstring"
#include"iostream"
#include"algorithm"
using namespace std;

const int MAXN=1e5+5;

int n,T,mx,hd,tl;
char ch[MAXN];
int id[MAXN],rnk[MAXN],SA[MAXN],bnk[MAXN],Ht[MAXN];
int cnt[MAXN],q[MAXN];

int read()
{
    int x=0;char ch=getchar();
    while(ch<'0'||'9'<ch) ch=getchar();
    while('0'<=ch&&ch<='9') x=(x<<3)+(x<<1)+(ch^48),ch=getchar();
    return x;
}

void shel()
{
    for(int i=1;i<=n;++i) ++bnk[rnk[i]];
    for(int i=1;i<=mx;++i) bnk[i]+=bnk[i-1];
    for(int i=1;i<=n;++i) SA[++bnk[rnk[id[i]]-1]]=id[i];
    for(int i=0;i<=mx;++i) bnk[i]=0;
}

void GetSA()
{
    mx=0;
    for(int i=1;i<=n;++i) id[i]=i,rnk[i]=ch[i],mx=mx<rnk[i]?rnk[i]:mx;
    shel();
    for(int k=1;k<n;k<<=1){
        for(int i=1;i<=k;++i) id[i]=n-k+i;
        int ct=k;
        for(int i=1;i<=n;++i) if(SA[i]>k) id[++ct]=SA[i]-k;
        shel();swap(rnk,id);rnk[SA[1]]=1;
        for(int i=2;i<=n;++i){
            if(id[SA[i]]==id[SA[i-1]]&&id[SA[i]+k]==id[SA[i-1]+k]) rnk[SA[i]]=rnk[SA[i-1]];
            else rnk[SA[i]]=rnk[SA[i-1]]+1;
        }if(rnk[SA[n]]==n) break;
        mx=rnk[SA[n]];
    }return;
}

void GetHt()
{
    int k=0;
    for(int i=1;i<=n;++i){
        if(rnk[i]==1) continue;
        int tmp=SA[rnk[i]-1];
        k=k?k-1:0;
        while(tmp+k<=n&&i+k<=n&&ch[i+k]==ch[tmp+k]) ++k;
        Ht[rnk[i]]=k;
    }return;
}

int GetLCP(int x,int y)
{
    if(x>y) return n-SA[y]+1;
    return Ht[q[hd]];
}

int main()
{
    T=read();
    while(T--){
        memset(id,0,sizeof(id));
        memset(cnt,0,sizeof(cnt));
        scanf("%s",ch+1);n=strlen(ch+1);
        int w;scanf("%d",&w);Ht[n+1]=0;
        GetSA(),GetHt();hd=1;tl=0;
        for(int i=2;i<=w;++i){
            while(hd<=tl&&Ht[q[tl]]>=Ht[i]) --tl;
            q[++tl]=i;
        }for(int i=w;i<=n;++i){
            if(i-q[hd]+1>=w) ++hd;
            while(hd<=tl&&Ht[q[tl]]>=Ht[i]) --tl;
            q[++tl]=i;
            int tmp=GetLCP(i+1,i+w-1);
            int g=max(Ht[i-w+1],Ht[i+1]);
            if(g<=tmp) ++cnt[g+1],--cnt[tmp+1];
        }int tmp=-1,mm=1;
        for(int i=1;i<=n;++i){
            cnt[i]+=cnt[i-1];
            if(cnt[i]>=mm) mm=cnt[i],tmp=i;
        }printf("%d\n",tmp);
    }return 0;
}