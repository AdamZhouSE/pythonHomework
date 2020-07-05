#include<bits/stdc++.h>
using namespace std;
struct Node {
    int v; // 值
    Node *l=NULL, *r=NULL; // 左右子树
};
vector<int> in, post; // 中序，后序存储
int minSum=0x3fffff, ans=-1; // 路径最小和，答案
Node* createTree(int i1, int j1, int i2, int j2) { // 建树-- in:[i1,j1) post:[i2,j2)
    if (i1 >= j1 || i2 >= j2) return NULL; // 空树
    Node* root = new Node;
    root->v = post[j2-1]; // 后序结尾为个
    int j = find(in.begin()+i1, in.begin()+j1, post[j2-1]) - in.begin(); // 在in中查找
    root->l = createTree(i1, j, i2, i2+(j-i1)); // 左子树建立
    root->r = createTree(j+1, j1, i2+(j-i1), j2-1); // 右子树建立
    return root;
}
void dfs(Node* root, int sum) { // 计算到每个叶子的路径和并记录最小者
    if (root->l == NULL && root->r == NULL) { // 叶子
        sum += root->v;
        if (sum < minSum || (sum == minSum && ans > root->v)) { // 总和最小；若相同去叶子值最小者
            minSum = sum;
            ans = root->v;
        }
        return;
    }
    if (root->l != NULL) dfs(root->l, root->v+sum); // 非空，则访问左子树
    if (root->r != NULL) dfs(root->r, root->v+sum); // 非空，则访问右子树
}
int main() {
    string s1, s2, st;
    while (getline(cin, s1) && getline(cin, s2)) {
        in.clear(); post.clear(); // 初始化
        stringstream input1(s1), input2(s2);
        while (input1 >>st) in.push_back(stoi(st)); // 中序存储
        while (input2 >>st) post.push_back(stoi(st)); // 后续存储
        Node* btree = createTree(0, in.size(), 0, post.size()); // 建树
        minSum=0x3fffff; dfs(btree, 0); // 遍历计算
        printf("%d\n", ans);
    }
    return 0;
}

ahhxzyc • 1 months ago Reply • Edit • Delete 
不建树，在序列上搜索
#include <iostream>
#include <vector>
#include <sstream>
using namespace std;
const int INF = 2e9;

vector<int> inV, postV;
int minVal, minLeaf;

void dfs(int inStart, int postStart, int len, int val) {
    if(len < 1) return;
    if(len == 1) {
        int leaf = inV[inStart]; val += leaf;
        if(val < minVal || val == minVal && leaf < minLeaf) {
            minVal = val;
            minLeaf = leaf;
        }
        return;
    }
    int root = postV[postStart + len - 1], k = inStart;
    while(inV[k] != root) k++;
    dfs(inStart, postStart, k-inStart, val+root);
    dfs(k+1, postStart+k-inStart, inStart+len-k-1, val+root);
}

bool readLine(vector<int> &v) {
    string line;
    if(!getline(cin, line)) return false;
    stringstream ss(line);
    int x; v.clear();
    while(ss >> x) v.push_back(x);
    return true;
}

int main() {
    while(readLine(inV)) {
        readLine(postV);
        minVal = minLeaf = INF;
        dfs(0,0,inV.size(),0);
        cout << minLeaf << endl;
    }
    return 0;
}