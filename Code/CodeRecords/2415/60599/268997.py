
#include<iostream>
using namespace std;
 
int dp[35][35],pre[35][35];
void print(int l,int r);
 
int main()
{
    int n;
    int score[31];
    int len,i,j,k;
    int x;
    
    cin>>n;//输入节点数
    for(i=1;i<=n;i++)//输入节点分数
        cin>>score[i];
    
    for(i=1;i<=n;i++)
    {
        dp[i][i]=score[i];//存储子树的最大加分
        pre[i][i]=i;//存储根节点
    }
    
    for(len=1;len<=n;len++)//len:子树结点数
    {
        for(i=1;i+len<=n;i++)//子树最左端的结点 
        {
            j=len+i;//子树最右端的结点 
            x=score[j]+dp[i][j-1];//j加仅一棵子树的情况 
            dp[i][j]=score[i]+dp[i+1][j];//i加仅一棵子树的情况 
            pre[i][j]=i;
            if(dp[i][j]<x)
            {
                dp[i][j]=x;
                pre[i][j]=j;
            }
            for(k=i+1;k<j;k++)//两棵子树的情况,k:根节点 
            {
                x=score[k]+dp[i][k-1]*dp[k+1][j];
                if(dp[i][j]<x)
                {
                    dp[i][j]=x;
                	pre[i][j]=k;
                }
            } 
        }
    }
    
    cout<<dp[1][n]<<endl;//输出最高加分
    print(1,n);//输出前序
    return 0;
}
 
void print(int l,int r)
{
    if(l>r)
        return;
    cout<<pre[l][r]<<" ";//根结点输出
    if(l==r) 
        return;
    print(l,pre[l][r]-1);
    print(pre[l][r]+1,r);
}