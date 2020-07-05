#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

struct TreeNode{
    char data;
    TreeNode* leftChild;
    TreeNode* rightChild;
};

int search(string str, char ch) {
    for (int i = 0; i < str.length(); i++) {
        if (ch == str[i])
            return i;
    }
    return -1;
}

//分治+递归，每次取前序的第一位，在中序中找到它，并把中序以它为切割点分成两半
TreeNode* Create(string PreO, string InO){
    if(PreO.length()==0)
        return NULL;
    TreeNode* root = new TreeNode;
    char ch =PreO[0];//取当前前序第一个ch
    root->data = ch;//赋值

    int pos = search(InO, ch);//在中序遍历中找到这个ch，并返回位置
    int leftNumber = pos;//有i个节点在它左边
    int rightNumber = InO.length()-pos -1;//有InO.length()-pos-1个节点在它右边
    string leftInO = InO.substr(0,leftNumber);//从InO[0]到InO[pos-1]
    string rightInO = InO.substr(pos+1);//InO[pos+1]到结尾
    string leftPreO = PreO.substr(1,leftNumber);
    string rightPreO = PreO.substr(pos+1);

    root->leftChild = Create(leftPreO, leftInO);
    root->rightChild = Create(rightPreO, rightInO);

    return root;
}

//后序遍历
void PostOrder(TreeNode* root){
    if(root==NULL)
        return ;
    PostOrder(root->leftChild);
    PostOrder(root->rightChild);
    cout<<root->data;
    return ;
}

int main() {
    string pre, in;
    while (cin >> pre) {
        cin >> in;
        TreeNode *root = new TreeNode;
        root = Create(pre, in);
        PostOrder(root);
        cout << endl;
    }
    return 0;
}