

#include<bits/stdc++.h>
using namespace std;
struct TreeNode{
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int value):val(value),left(nullptr),right(nullptr){}
};
// 建树
void createTree(TreeNode* root,int cnt)
{
    if(!cnt) return;
    int p,l,r;
    cin>>p>>l>>r;
    if(l)
    {
         TreeNode* left = new TreeNode(l);
         root->left = left;
         createTree(root->left,cnt-1);
    }
    if(r)
    {
        TreeNode* right = new TreeNode(r);
        root->right = right;
        createTree(root->right,cnt-1);
    }
    
}
// 前序非递归
void preOrder(TreeNode* root,vector<int>& ans)
{
    if(!root) return;
    stack<TreeNode*>s;
    TreeNode* p = root;
    while(!s.empty() || p)
    {
// 一直往左走
        while(p)
        {
// 先访问再入栈
            ans.push_back(p->val);
            s.push(p);
            p = p->left;
        }
                // 已经到最左边，出栈一个结点
        p = s.top();
        s.pop();
                // 如果当前结点有右子树，则进入右子树
        if(p->right) p = p->right;
                // 否则将访问指针p置空
        else p = nullptr;
    }
}
// 中序非递归
void inOrder(TreeNode* root,vector<int>& ans)
{
    if(!root) return;
    stack<TreeNode*>s;
    TreeNode* p = root;
    while(!s.empty() || p)
    {
                 
        while(p)
        {
            s.push(p);
            p = p->left;
        }
                // 此处与先序不同，这里是先入栈，出栈的时候再访问
        p = s.top();
        ans.push_back(p->val);
        s.pop();
        if(p->right) p = p->right;
        else p = nullptr;
    }
}
// 后序非递归
void postOrder(TreeNode* root,vector<int>& ans)
{
    if(!root) return ;
    stack<TreeNode*>s;
    TreeNode* p = root;
        // 与先序中序有所不同，使用了一个标志量来保存刚刚访问过的结点
    TreeNode* r = nullptr;
    while(!s.empty() || p)
    {
 
                // 一直向左
        while(p)
        {
            s.push(p);
            p = p->left;
        }
        p = s.top();
                // 如果当前结点有右子树并且不是刚访问过，则访问右子树
        if(p->right && p->right!=r) p = p->right;
        else{
                      // 否则 访问当前结点
                       // 并利用标志变量记录下来
                        // 访问指针p置空，很关键
            s.pop();
            ans.push_back(p->val);
            r = p;
            p = nullptr;
        }
    }
}
int main()
{
    int N,root_val;
    cin>>N>>root_val;
    TreeNode* root = new TreeNode(root_val);
    createTree(root,N);
    vector<int>ans;
    preOrder(root,ans);
    for(int i : ans)
        cout<<i<<" ";
    cout<<endl;
    ans.clear();
    inOrder(root,ans);
    for(int i:ans)
        cout<<i<<" ";
    cout<<endl;
    ans.clear();
    postOrder(root,ans);
    for(int i:ans)
        cout<<i<<" ";
    cout<<endl;
    return 0;
}
