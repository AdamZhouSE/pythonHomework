
#include<iostream>
#include<vector>
#include<unordered_map>
#include<queue>
using namespace std;
 
struct TreeNode
{
    int value;
    TreeNode* lchild;
    TreeNode* rchild;
    TreeNode(int value)
        : value(value), lchild(nullptr), rchild(nullptr) {}
};
 
TreeNode* createNode(unordered_map<int, vector<int>>& datas, int value)
{
    TreeNode* newnode = nullptr;
     
    if (value != 0)
    {
        newnode = new TreeNode(value);
        newnode->lchild = createNode(datas, datas[value][0]);
        newnode->rchild = createNode(datas, datas[value][1]);
    }
    return newnode;
 
}
void InOrder(TreeNode* root, queue<TreeNode*>& q)
{
    if (root == nullptr)
        return;
    InOrder(root->lchild,q);
    q.push(root);
    InOrder(root->rchild,q);
}
int main()
{
    int n;
    cin >> n;
    unordered_map<int, vector<int>> datas;
    int rfa, rlch, rrch;
    cin >> rfa >> rlch >> rrch;
    datas[rfa] = vector<int>{ rlch,rrch };
    for (int i = 1; i < n; i++)
    {
        int fa, lch, rch;
        cin >> fa >> lch >> rch;
        datas[fa] = vector<int>{ lch,rch };
    }
    TreeNode* root = createNode(datas, rfa);
    queue<TreeNode*> q;
    InOrder(root,q);
    TreeNode L(-1);
    root = &L;
    while (!q.empty())
    {
        TreeNode* tmp = q.front();
        tmp->lchild = root;
        tmp->rchild = nullptr;
        root->rchild = tmp;
        root = tmp;
        q.pop();
    }
    root = L.rchild;
    while (root != nullptr)
    {
        cout << root->value << " ";
        root = root->rchild;
    }
    cout << endl;
}
