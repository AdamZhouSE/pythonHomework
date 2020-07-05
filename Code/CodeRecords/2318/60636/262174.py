链接：https://www.nowcoder.com/questionTerminal/380d49d7f99242709ab4b91c36bf2acc
来源：牛客网

#include<bits/stdc++.h>
using namespace std;
struct ReturnType{
    int maxBSTHead;
    int maxBSTSize;
    int MIN;
    int MAX;
    ReturnType(int root,int size,int Min,int Max):maxBSTHead(root),maxBSTSize(si***(Min),MAX(Max){}
};
ReturnType process(int root,int* lc,int* rc)
{
    // base case 注意最大最小值的赋值
    if(!root) return ReturnType(0,0,INT_MAX,INT_MIN);
    // 搜集到左右子树的信息
    ReturnType ldata = process(lc[root],lc,rc);
    ReturnType rdata = process(rc[root],lc,rc);
    // 整合
    // 以当前结点为根的最大值与最小值
    int max_ = max(root,max(ldata.MAX,rdata.MAX));
    int min_ = min(root,min(ldata.MIN,rdata.MIN));
    // 最大搜索二叉子树来源于左子树或右子树
    int curMaxBSTHead = ldata.maxBSTSize>rdata.maxBSTSize ? ldata.maxBSTHead:rdata.maxBSTHead;
    int curMaxBSTSize = max(ldata.maxBSTSize,rdata.maxBSTSize);
    // 要把根节点加入进去的情况
    if(ldata.maxBSTHead == lc[root] && rdata.maxBSTHead == rc[root] && root>ldata.MAX && root<rdata.MIN)
    {
        curMaxBSTHead = root;
        curMaxBSTSize = 1 + ldata.maxBSTSize + rdata.maxBSTSize;
    }
    return ReturnType(curMaxBSTHead,curMaxBSTSi***_,max_);
}
int main()
{
    int n,root;
    cin>>n>>root;
    int* lc = new int[n+1];
    int* rc = new int[n+1];
    int p;
    for(int i=0;i<n;++i)
    {
        cin>>p;
        cin>>lc[p]>>rc[p];
    }
    int ans = process(root,lc,rc).maxBSTSize;
    cout<<ans<<endl;
 
    return 0;
}