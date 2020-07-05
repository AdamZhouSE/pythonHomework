#include<bits/stdc++.h>
using namespace std;
int n;//二叉树节点数
struct tree//二叉树 
{
    int fa;//父亲节点 
    int l;//左孩子 
    int r;//右孩子 
}tr[100005];
int w[100005];//结点的数值 
int inord[100005];//中序遍历 
int k;
int lis[100005];//最长不降子序列
void inorder(int root)//中序遍历 
{
    if(tr[root].l)//如果左儿子不为空 
        inorder(tr[root].l);//搜索左儿子 
    inord[++k]=w[root]-k;
    if(tr[root].r)//如果右儿子不为空 
        inorder(tr[root].r);//搜索右儿子 
}
int main()
{
    cin>>n;//输入n个结点 
    for(int i=1;i<=n;i++)
        cin>>w[i];//输入每个人结点的数值 
    tr[1].fa=0;//1号点的父亲为空 
    for(int i=2;i<=n;i++)
    {
        int t;//左/右儿子 
        cin>>tr[i].fa>>t;//输入父亲结点 
        if(t==0) 
            tr[tr[i].fa].l=i;//这个点是他父亲的左儿子 
        else
            tr[tr[i].fa].r=i;//这个点是他父亲的右儿子 
    }
    inorder(1);//对这棵树进行中序遍历 
    lis[1]=inord[1];//求最长不下降序列 
    int cnt=1;//最长不下降序列长度 
    for(int i=2;i<=n;i++)
    {
        if(inord[i]>=lis[cnt])
            lis[++cnt]=inord[i];
        else
        {
            int j=lower_bound(lis+1,lis+1+cnt,inord[i])-lis;//lower_bound返回的是在lis的1~1+cnt的范围内第一个大于等于inord[i]的数的位置 
            lis[j]=inord[i]; 
        }   
    } 
    cout<<n-cnt<<endl;//总个数-最长不下降序列长度，就是要修改的个数 
}