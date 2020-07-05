#include<bits/stdc++.h>
#define LL long long
#define _(d) while(d(isdigit(ch=getchar())))
using namespace std;
int R(){
    int x;bool f=1;char ch;_(!)if(ch=='-')f=0;x=ch^48;
    _()x=(x<<3)+(x<<1)+(ch^48);return f?x:-x;}
const int N=2e5+5;
int n,m,w[N],p[N],ht[N],rak[N],tp[N],sa[N],tax[N],ans;
char ch[N];
void Qsort(){
    for(int i=0;i<=m;i++)tax[i]=0;
    for(int i=1;i<=n;i++)tax[rak[tp[i]]]++;
    for(int i=1;i<=m;i++)tax[i]+=tax[i-1];
    for(int i=n;i>=0;i--)sa[tax[rak[tp[i]]]--]=tp[i];
}
void SA(){
    m=26,Qsort();
    for(int l=1,p=0;l<=n;l<<=1){
        for(int i=n-l+1;i<=n;i++)tp[++p]=i;
        for(int i=1;i<=n;i++)if(sa[i]>l)tp[++p]=sa[i]-l;
        Qsort(),swap(rak,tp);
        rak[sa[1]]=p=1;
        for(int i=2;i<=n;i++)
            rak[sa[i]]=(tp[sa[i-1]]==tp[sa[i]]&&tp[sa[i-1]+l]==tp[sa[i]+l])?p:++p;
        if(p>n)break;
        m=p+1,p=0;
    }
    int k=0;
    for(int i=1,j;i<=n;i++){
        j=sa[rak[i]-1];
        if(k)k--;
        while(ch[j+k]==ch[i+k])k++;
        ht[rak[i]]=k;
    }
}
bool cmp(int a,int b){return ht[a]>ht[b];}
int li[N],ri[N],fa[N],rt[N],tot,tr[N*50][2];
int query(int k,int dep,int val){
    if(!~dep)return 0;
    if(tr[k][((val>>dep)&1)^1])
        return (1<<dep)+query(tr[k][((val>>dep)&1)^1],dep-1,val);
    else return query(tr[k][(val>>dep)&1],dep-1,val);
}
void insert(int &k,int dep,int val){
    if(!k)k=++tot;
    if(~dep)insert(tr[k][(val>>dep)&1],dep-1,val);
}
int merge(int x,int y){
    int res=0;
    if(ri[x]-li[x]<ri[y]-li[y])swap(x,y);
    for(int i=li[y];i<=ri[y];i++)
        res=max(res,query(rt[x],17,w[sa[i]]));
    for(int i=li[y];i<=ri[y];i++)
        insert(rt[x],17,w[sa[i]]);
    fa[y]=x,li[x]=min(li[x],li[y]),ri[x]=max(ri[x],ri[y]);
    return res;
}
int find(int x){return fa[x]==x?x:fa[x]=find(fa[x]);}
int main(){
    n=R(),scanf("%s",ch+1);
    for(int i=1;i<=n;i++)
        rak[i]=ch[i]-'a',p[i]=tp[i]=i,w[i]=R();
    SA(),sort(p+2,p+n+1,cmp);
    for(int i=1;i<=n;i++)
        li[i]=ri[i]=fa[i]=i,insert(rt[i],17,w[sa[i]]);
    for(int i=2;i<=n;i++)
        ans=max(ans,ht[p[i]]+merge(find(p[i]-1),find(p[i])));
    cout<<ans<<endl;
    return 0;
}