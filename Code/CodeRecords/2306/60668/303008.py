
#include <iostream>
#include <vector>
using namespace std;
 
struct TreeNode {
    long val;
    TreeNode*left;
    TreeNode*right;
    TreeNode(long v): val(v), left(nullptr), right(nullptr) {}
};
 
void makeTree(TreeNode* root, long cnt) {
    if (cnt == 0) return;
    long p, l, r;
    cin >> p >> l >> r;
    if (l != 0) {
        TreeNode* left = new TreeNode(l);
        root -> left = left;
        makeTree(left, cnt - 1);
    }
    if (r != 0) {
        TreeNode* right = new TreeNode(r);
        root -> right = right;
        makeTree(right, cnt - 1);
    }
}
 
void preOrder(TreeNode* root, vector<long> &res) {
    if (root == nullptr) return;
    res.push_back(root -> val);
    preOrder(root->left, res);
    preOrder(root->right, res);
}
 
void midOrder(TreeNode* root, vector<long> &res) {
    if (root == nullptr) return;
    midOrder(root -> left, res);
    res.push_back(root -> val);
    midOrder(root->right, res);
}
 
void postOrder(TreeNode* root, vector<long> &res) {
    if (root == nullptr) return;
    postOrder(root -> left, res);
    postOrder(root -> right, res);
    res.push_back(root -> val);
}
 
int main() {
    long N, first;
    cin >> N >> first;
    TreeNode* root = new TreeNode(first);
    makeTree(root, N);
    vector<long> res;
    preOrder(root, res);
     
    int len = res.size();
    for (int i = 0; i < len; i++) {
        cout << res[i] << " ";
    }
    cout << endl;
     
    res.clear();
    midOrder(root, res);
    len = res.size();
    for (int i = 0; i < len; i++) {
        cout << res[i] << " ";
    }
    cout << endl;
     
    res.clear();
    postOrder(root, res);
    len = res.size();
    for (int i = 0; i < len; i++) {
        cout << res[i] << " ";
    }
    cout << endl;
    return 0;
}