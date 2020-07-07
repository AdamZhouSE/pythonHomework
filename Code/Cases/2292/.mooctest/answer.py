#include <cstdio>
#include <stack>
#include <algorithm>
#include <map>
 
using namespace std;
 
struct binaryTreeNode
{
    int element;
    binaryTreeNode *leftChild, *rightChild;
};
 
binaryTreeNode* ConstructTree(const int numbers[], const int length)
{
    if (length < 3 || length % 3 != 0)
        return NULL;
 
    binaryTreeNode *root = new binaryTreeNode{ numbers[0],NULL,NULL };
    stack<binaryTreeNode **> s;
    s.push(&root);
 
    int i = 0;
    while (!s.empty())
    {
        binaryTreeNode **t = s.top();
        s.pop();
 
        if (numbers[i + 2] != 0)
        {
            (*t)->rightChild = new binaryTreeNode{ numbers[i + 2],NULL,NULL };
            s.push(&((*t)->rightChild));
        }
 
        if (numbers[i + 1] != 0)
        {
            (*t)->leftChild = new binaryTreeNode{ numbers[i + 1],NULL,NULL };
            s.push(&((*t)->leftChild));
        }
 
        i += 3;
    }
 
    return root;
}
 
int maxTopo(binaryTreeNode *src, binaryTreeNode *dst);
bool isBSTNode(binaryTreeNode *src, binaryTreeNode *dst);
 
int bstTopoSize1(binaryTreeNode *root)
{
    if (root == NULL)
        return 0;
 
    int maxSize = 0;
    int curSize = maxTopo(root, root);
    if (maxSize < curSize)
        maxSize = curSize;
 
    if (root->leftChild != NULL)
    {
        int curSize = bstTopoSize1(root->leftChild);
        if (maxSize < curSize)
            maxSize = curSize;
    }
    if (root->rightChild != NULL)
    {
        int curSize = bstTopoSize1(root->rightChild);
        if (maxSize < curSize)
            maxSize = curSize;
    }
 
    return maxSize;
}
 
 
int maxTopo(binaryTreeNode *src, binaryTreeNode *dst)
{
    if (src != NULL && dst != NULL && isBSTNode(src, dst))
        return 1 + maxTopo(src, dst->leftChild) + maxTopo(src, dst->rightChild);
 
    return 0;
}
 
bool isBSTNode(binaryTreeNode *src, binaryTreeNode *dst)
{
    if (src == NULL || dst == NULL)
        return false;
    if (src == dst)
        return true;
 
    if (src->element < dst->element)
        return isBSTNode(src->rightChild, dst);
    else
        return isBSTNode(src->leftChild, dst);
}
 
int main(int argc, char *argv[])
{
    int n, rootValue;
    scanf("%d %d", &n, &rootValue);
 
    int *numbers = new int[3 * n];
    for (int i = 0; i < 3 * n; ++i)
        scanf("%d", numbers + i);
 
    binaryTreeNode *root = ConstructTree(numbers, 3 * n);
 
    int size = bstTopoSize1(root);
 
    printf("%d\n", size);
 
    return 0;
}