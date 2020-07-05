
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
const int N=4*1e4+10;const int K=5*1e5+10;const int NK=6*1e7+10;
inline void clear(vector <int>& ve){vector <int> emp;swap(emp,ve);}//高速清空函数 
vector <int> v[N];int w[N];int a[N];int n;int res;int ctt;int k;
int dfn1[N];int dfn2[N];int df1;int df2;int siz[N];int line[N];
int dp1[NK];int dp2[NK];bool lf[N];int nfd1[N];int nfd2[N];int T;
int h;int fa[N];int q1[2*K];int q2[2*K];int hed=1;int til=0;
inline void dypr(int* dfn,int* dp)//dp的函数 
{
    for(int i=1;i<=ctt;i++)
    {
        int v=dfn[i];hed=1;til=1;q1[til]=q2[til]=0;//手动inline了全部的deque操作，凑合着看吧 
        for(int j=1;j<=k;j++)
        {
            hed+=(q1[hed]<j-a[v])?1:0;int val=dp[(i-1)*(k+1)+j]-j*w[v];
            dp[i*(k+1)+j]=max(q2[hed]+j*w[v],dp[(i-siz[v])*(k+1)+j]);//单调队列优化转移 
            while(hed<=til&&q2[til]<=val){til--;}q1[++til]=j;q2[til]=val;
        }
    }
}
inline void clear_all()//清空函数 
{
    for(int i=0;i<=ctt;i++){clear(v[i]);lf[i]=line[i]=siz[i]=0;}
    for(int i=0;i<=(ctt+1)*(k+1);i++){dp1[i]=dp2[i]=0;}
    df1=df2=res=ctt=0;h=0;
}
void dfs1(int x)//正着dfs，原谅我毒瘤压行 
{
    siz[x]=1;
    for(int i=0;i<v[x].size();i++)
    {dfs1(v[x][i]);siz[x]+=siz[v[x][i]];}dfn1[++df1]=x;nfd1[x]=df1;
}
void dfs2(int x)//reverse后dfs 
{
    for(int i=v[x].size()-1;i>=0;i--)
    {line[v[x][i]]=line[x]+w[v[x][i]];dfs2(v[x][i]);}
    dfn2[++df2]=x;nfd2[x]=df2;
}
inline void solve()
{
    scanf("%d%d",&n,&k);ctt=n;
    for(int i=1;i<=n;i++){scanf("%d%d%d",&fa[i],&a[i],&w[i]);lf[fa[i]]=true;}
    for(int i=1;i<=n;i++)//加边和拆点 
    {
        v[fa[i]].push_back(i);
        if(a[i]>1){a[++ctt]=a[i]-1;a[i]=1;w[ctt]=w[i];v[i].push_back(ctt);}
    }line[1]=w[1];dfs1(1);dfs2(1);dypr(dfn1,dp1);dypr(dfn2,dp2);//dfs和dp 
    for(int i=1;i<=n;i++)//枚举叶子更新答案 
    {
        if(lf[i])continue;
        for(int j=0;j<=k;j++)
        {res=max(res,dp1[(nfd1[i]-1)*(k+1)+j]+line[i]+dp2[(nfd2[i]-siz[i])*(k+1)+(k-j)]);}
    }printf("%d\n",res);//然后靠信仰卡常吧 
}
int main()
{scanf("%d",&T);for(int z=1;z<=T;z++){solve();clear_all();}return 0;}