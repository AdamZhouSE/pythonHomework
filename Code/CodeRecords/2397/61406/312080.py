#include<cstdio>
#include<vector>
#include<iostream>
using namespace std;
const int maxn=1500;
int a[4][50][50];
int vis[maxn][maxn];
int dp[maxn][4][maxn];
struct ss{
    vector<int>nei;//相当于编表 
    ss(){
        nei.clear();
    }
}node[maxn];
int n,ans=0;
inline int read(){
    register int x=0,f=1;
    register char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-') f=-1;ch=getchar();}
    for(;ch>='0'&&ch<='9';ch=getchar()) x=x*10+ch-'0';
    return x*f;
}
void link(int a,int b){//建立点与点关系（用权值，不是编号） 
    if(!vis[a][b]){
        vis[a][b]=1;
        node[a].nei.push_back(b);//c[a][++c[a][0]]=b;
    }
    if(!vis[b][a]){
        vis[b][a]=1;
        node[b].nei.push_back(a);//c[b][++c[b][0]]=a;
    }
}
void first(){
    for(int k=0;k<=3;k++)//处理本区域内的关系 
        for(int i=2;i<n;i++)
            for(int j=2;j<i*2-1;j++){
                link(a[k][i][j],a[k][i][j-1]);
                link(a[k][i][j],a[k][i][j+1]);
                if(j%2==0)//处理某层的第奇偶个 
                    link(a[k][i][j],a[k][i-1][j-1]);//倒立的三角 
                else
                    link(a[k][i][j],a[k][i+1][j+1]);//正放的三角 
            }
    for(int k=0;k<=3;k++)//处理与D相接但在本区域内的
        for(int j=2;j<=n*2-1;j+=2){
            link(a[k][n][j],a[k][n][j-1]);
            link(a[k][n][j],a[k][n][j+1]);
            link(a[k][n][j],a[k][n-1][j-1]);
        }
    for(int k=1,i=1;k<=n;k++,i++){//处理结合处部分
        link(a[0][i][1],a[2][i][i*2-1]);
        link(a[0][i][i*2-1],a[1][i][1]);
        link(a[1][i][i*2-1],a[2][i][1]);
    }
    for(int j=1;j<=n*2-1;j+=2){//处理D的边界 
        link(a[0][n][j],a[3][n-(j/2)][1]);
        link(a[1][n][j],a[3][j/2+1][((j/2)+1)*2-1]);
        link(a[2][n][j],a[3][n][n*2-j]);
    }
}
int tree_dp(int i,int l1,int l2){//i:当前点的权值;l1:当前点父亲节点的权值;l2:限定范围 
    int from=0;
    while(node[i].nei[from]!=l2) from++;//寻找父亲节点编号，该方向不再遍历 
    if(dp[i][from][l1]>0) return dp[i][from][l1];//记忆化 
    int l,r;
    if(l1>l2)
        l=l2+1,r=l1;//左子树 
    else
        l=l1,r=l2-1;//右子树
    int lmax=0,rmax=0;
    for(int j=0;j<=2;++j){
        if(j!=from&&(l<=node[i].nei[j]&&node[i].nei[j]<=r))//满足范围 
            if(node[i].nei[j]<i)//判断向左还是向右 
                lmax=max(lmax,tree_dp(node[i].nei[j],l,i));//dp向下找左子树的最大节点数 
            else
                rmax=max(rmax,tree_dp(node[i].nei[j],r,i));//dp向下找左子树的最大节点数
    }
    return dp[i][from][l1]=lmax+rmax+1;//左子树+左子树+根 
}
void dfs(){
    for(int i=1;i<=n*n*4;i++){//遍历1-4*n^2的所有点 
        int lm=0,rm=0;
        for(int j=0;j<=2;j++){
            if(node[i].nei[j]<i)//见tree_dp
                lm=max(lm,tree_dp(node[i].nei[j],1,i));
            else
                rm=max(rm,tree_dp(node[i].nei[j],n*n*4,i));
        }
        ans=max(ans,lm+rm+1);//遍历 取最大值 
    }
}
int main(){
    n=read();
    for(int i=0;i<4;i++)//a[i][j][k];i:A,B,C,D区域编号;j:为该区域第几层;k:为该区域该层第几个 
        for(int j=1;j<=n;j++)
            for(int k=1;k<=2*j-1;k++)
                a[i][j][k]=read();
    first();//预处理 
    dfs();//记忆化搜索 
    printf("%d\n",ans);
    return 0;
}