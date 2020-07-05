#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ifstream in("input.txt");
ofstream out("output.txt");
#define debug(x) cerr<<#x<<" = "<<x<<endl
#define debugs(x,y) cerr<<#x<<" = "<<x<<"   "<<#y<<" = "<<y<<endl
const ll N=5e4+7;
const ll base=137;
const ll mod=21474836470000;
template<typename T>inline T read(T &x)
{
    x=0;ll f=1;char c;
    while(!isdigit(c=getchar()))if(c=='-')f=-1;
    while(isdigit(c)){x=(x<<1)+(x<<3)+(c^48);c=getchar();}
    return x*f;
}
ll in_order[N],post_order[N],lch[N],rch[N],n,m,best,best_sum;
inline bool read_list(ll *a)
{
    string line;
    if(!getline(cin,line))return false;
    stringstream ss(line);
    n=0;ll x;
    while(ss>>x)a[n++]=x;
    return n>0;
}
inline ll build(ll L1,ll R1,ll L2,ll R2)//利用数组来建树，用左儿子和右儿子两个数组存节点
{
    if(L1>R1)return 0;//如果就它一个就不用建了
    ll root=post_order[R2];//找到后序遍历的根
    ll p=L1;
    while(in_order[p]!=root)p++;//先找中序遍历的根
    ll cnt=p-L1;//左子树的结点数
    //利用后序遍历找每棵树的根
    //利用中序遍历把左子树和右子树分开
    lch[root]=build(L1,p-1,L2,L2+cnt-1);//以根为分界线分开作左右子树
    rch[root]=build(p+1,R1,L2+cnt,R2-1);//(R2-1):把根丢掉
    return root;
}
inline void dfs(ll u,ll sum)
{
    sum+=u;
    if(!lch[u]&&!rch[u])//如果两子树都为空说明找到叶子节点了
        if(sum<best_sum||(sum==best_sum&&u<best))
            best=u,best_sum=sum;//更新答案
    //否则就继续往下找叶子节点
    if(lch[u])dfs(lch[u],sum);//先左
    if(rch[u])dfs(rch[u],sum);//再右
}
int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    while(read_list(in_order))
    {
        read_list(post_order);
        build(0,n-1,0,n-1);
        best_sum=mod;
        dfs(post_order[n-1],0);//从根开始找，sum赋值为0
        cout<<best<<endl;
    }
    return 0;
}
