#include<bits/stdc++.h>
using namespace std;
struct Node{
    int lc = 0;
    int rc = 0;
    int parent = -1;
    int level;
};
// 确定每个结点所在层
void getNodeLevel(vector<Node>& tree,int root)
{
    if(!root) return;
    // 左子树各节点的level
    if(tree[root].lc)
    {
        tree[tree[root].lc].level = tree[root].level + 1;
        getNodeLevel(tree,tree[root].lc);
    }
    // 右子树各节点的level
    if(tree[root].rc)
    {
        tree[tree[root].rc].level = tree[root].level + 1;
        getNodeLevel(tree,tree[root].rc);
    }
    // 设置根节点的level
    if(tree[root].parent == -1)
        return;
    tree[root].level  = tree[tree[root].parent].level + 1;
}
int LCA(vector<Node>& tree,int o1,int o2)
{
    // 把层次深的节点一直沿父节点上移 直到两个节点处于同一level
    // 同一层次的节点同时沿各自的父节点上移，第一个相遇的节点就是LCA
    while(o1 != o2)
    {
        if(tree[o1].level>tree[o2].level)
            o1 = tree[o1].parent;
        else if(tree[o1].level<tree[o2].level)
            o2 = tree[o2].parent;
        else
        {
            o1 = tree[o1].parent;
            o2 = tree[o2].parent;
        }
    }
    return o1;
}
int main()
{
    int n,root;
    cin>>n>>root;
    vector<Node>tree(n+1);
    int pa,l,r;
    for(int i=0;i<n;++i)
    {
        cin>>pa;
        cin>>l>>r;
        tree[pa].lc = l;
        tree[pa].rc = r;
        if(l) tree[l].parent = pa;
        if(r) tree[r].parent = pa;
    }
    getNodeLevel(tree,root);
    int m;
    int o1,o2;
    cin>>m;
    while(m--)
    {
        cin>>o1>>o2;
        cout<<LCA(tree,o1,o2)<<endl;
    }
 
}