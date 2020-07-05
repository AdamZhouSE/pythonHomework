

#include<bits/stdc++.h>
using namespace std;
bool isBST(int root,int target,int* lc,int* rc)
{
    if(!root) return false;
    if(root==target) return true;
    return isBST(root > target ? lc[root]:rc[root],target,lc,rc);
}
int maxTopo(int root_1,int root_2,int* lc,int* rc)
{
    if(root_1 && root_2 && isBST(root_1,root_2,lc,rc))
        return maxTopo(root_1,lc[root_2],lc,rc) + maxTopo(root_1,rc[root_2],lc,rc) + 1;
    return 0;
}
void visit(int root,int* lc,int* rc,int& ans)
{
    if(!root) return;
    ans = max(ans,maxTopo(root,root,lc,rc));
    visit(lc[root],lc,rc,ans);
    visit(rc[root],lc,rc,ans);
}
int main()
{
    int n,root;
    cin>>n>>root;
    int p;
    int* lc = new int[n+1];
    int* rc = new int[n+1];
    for(int i=0;i<n;++i)
    {
        cin>>p;
        cin>>lc[p]>>rc[p];
    }
    int ans = 0;
    visit(root,lc,rc,ans);
    cout<<ans<<endl;
    return 0;
}