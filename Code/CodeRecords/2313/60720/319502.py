
#include<bits/stdc++.h>
using namespace std;
int InOrder(int root,int* lc,int* rc,int& pre)
{
    if(!root) return 1;
    int res = InOrder(lc[root],lc,rc,pre);
    if(root<pre) return 0;
    pre = root;
    if(res) return InOrder(rc[root],lc,rc,pre);
    else return 0;
}
int isBST(int root,int* lc,int* rc)
{
    if(!root) return 1;
    int pre = INT_MIN;
    return InOrder(root,lc,rc,pre) ? 1 : 0;
}
int isCBT(int root,int* lc,int* rc)
{
    if(!root) return 1;
    queue<int>q;
    q.push(root);
    while(!q.empty())
    {
        int cur = q.front();
        q.pop();
        if(!cur) break;
        q.push(lc[cur]);
        q.push(rc[cur]);
    }
    while(!q.empty())
    {
        if(q.front()) return 0;
        q.pop();
    }
    return 1;
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
    cout<<(isBST(root,lc,rc) ? "true" : "false")<<endl;
    cout<<(isCBT(root,lc,rc) ? "true" : "false")<<endl;
    return 0;
 
}