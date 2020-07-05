#include <iostream>
#include <string>
using namespace std;
string str;
int i;
struct TreeNode{
    char val;
    struct TreeNode *lchild, *rchild;
    TreeNode(char c) :val(c), lchild(NULL), rchild(NULL) {}
};
TreeNode* createTree() {
    char c = str[i++];
    if (c == '#') return NULL;
    TreeNode *root = new TreeNode(c);
    root->lchild = createTree();
    root->rchild = createTree();
    return root;
}

void inOrderTraversal(TreeNode* root) {
    if (!root) return;
    inOrderTraversal(root->lchild);
    cout << root->val << " ";
    inOrderTraversal(root->rchild);
}
int main() {
    while (cin >> str) {
        i = 0;
        TreeNode *root = createTree();
        inOrderTraversal(root);
        cout << "";
    }
    return 0;
}