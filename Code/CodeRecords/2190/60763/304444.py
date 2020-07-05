#include<set>
#include<map>
#include<cmath>
#include<vector>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#define pb push_back
#define fi first
#define se second
#define mp make_pair
using namespace std;

typedef double db;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pi;

const int N=200005;

int tot=1,la,ch[N][26],fa[N],len[N],ar[N],sz[N],rk[N],cnt[N];

void extend(int id)
{
    int p=la;
    int np=++tot;
    len[np]=len[p]+1;
    while(p && !ch[p][id])
    {
        ch[p][id]=np;
        p=fa[p];
    }
    if(!p)
    {
        fa[np]=1;
    }
    else
    {
        int q=ch[p][id];
        if(len[p]+1==len[q])
        {
            fa[np]=q;
        }
        else
        {
            int nq=++tot;
            fa[nq]=fa[q];
            len[nq]=len[p]+1;
            for(int i=0; i<26; i++)
                ch[nq][i]=ch[q][i];
            fa[np]=nq;
            fa[q]=nq;
            while(p && ch[p][id]==q)
            {
                ch[p][id]=nq;
                p=fa[p];
            }
        }
    }
    ++sz[la=np];
}

void Sort()
{
    for(int i=1; i<=tot; i++) ar[len[i]]++;
    for(int i=1; i<=tot; i++) ar[i]+=ar[i-1];
    for(int i=1; i<=tot; i++) rk[ar[len[i]]--]=i;
}

int T,n,k,mx,ans;

char S[N];

int main()
{
    scanf("%d",&T);
    while(T--)
    {
        scanf("%s%d",S+1,&k);
        n=strlen(S+1);
        la=1;
        for(int i=1; i<=n; i++) extend(S[i]-'a');
        Sort();
        auto upd=[](int l,int r){cnt[l]++;cnt[r+1]--;};
        for(int i=tot; i!=1; i--)
        {
            int now=rk[i];
            sz[fa[now]]+=sz[now];
            if(sz[now]==k) upd(len[fa[now]]+1,len[now]);
        }
        mx=ans=-1;
        for(int i=1; i<=n; i++)
        {
            cnt[i]+=cnt[i-1];
            if(cnt[i]>=mx)
            {
                mx=cnt[i];
                ans=i;
            }
        }
        printf("%d\n",mx>0?ans:-1);
        for(int i=1; i<=tot; i++)
        {
            len[i]=fa[i]=sz[i]=ar[i]=0;
            memset(ch[i],0,sizeof(ch[i]));
        }
        tot=1;
        for(int i=0; i<=n+1; i++) cnt[i]=0;
    }
    return 0;
}