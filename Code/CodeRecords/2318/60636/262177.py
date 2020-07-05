#include <bits/stdc++.h>
#define maxn 1000001
using namespace std;
 
struct Node{
    int val;
    Node* left;
    Node* right;
};
 
Node nodes[maxn];
struct Data{
    int min;
    int max;
    int size;
    Node* head;
    Data(int mi, int ma, int nod, Node* hea){
        min = mi;
        max = ma;
        size = nod;
        head = hea;
    }
};
 
Data process(Node* root){
    if(root == NULL){
        return Data(INT_MAX, INT_MIN, 0, root);
    }
    Data leftNode = process(root->left);
    Data rightNode = process(root->right);
    int together = 0;
    if(leftNode.head == root->left 
       && rightNode.head == root->right 
       && leftNode.max < root->val 
       && rightNode.min > root->val
      ) {
        together = leftNode.size + rightNode.size + 1;
    }
    int maxSize = max(max(leftNode.size, rightNode.size), together);
    Node* maxHead = leftNode.size > rightNode.size ? leftNode.head : rightNode.head;
    if(maxSize == together) {
        maxHead = root;
    }
    return Data(min(min(leftNode.min,rightNode.min),root->val),
                max(max(leftNode.max,rightNode.max),root->val),
                maxSize,
                maxHead);
}
int main()
{
    int n,r;
    scanf("%d%d",&n,&r);
    for(int i=0;i<n;i++){
        int index,left,right;
        scanf("%d%d%d",&index,&left,&right);
        nodes[index].val = index;
        if(left)
            nodes[index].left = &nodes[left];
        else
            nodes[index].left = NULL;
        if(right)
            nodes[index].right = &nodes[right];
        else
            nodes[index].right = NULL;
    }
    int res = process(&nodes[r]).size;
    printf("%d\n",res);
    return 0;
}