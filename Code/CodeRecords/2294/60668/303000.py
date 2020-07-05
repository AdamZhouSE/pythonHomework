#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#define N 1005
using namespace std;
vector<char> V;     //存放父节点
char pre[N], in[N]; //先序数组和后序数组
void make(int preleft, int preright, int inleft, int inright)
{
    int parent, leftsize, rightsize;
    for (parent = inleft; parent <= inright; parent++)
        if (in[parent] == pre[preleft])
            break; //找到父节点在中序遍历的位置parent
    leftsize = parent - inleft;
    rightsize = inright - parent; //获得左树和右树的大小
    if (leftsize > 0)
        make(preleft + 1, preleft + leftsize, inleft, parent - 1); //如果有左子树,递归重建左子树
    if (rightsize > 0)
        make(preleft + leftsize + 1, preright, parent + 1, inright); //如果有右子树,递归重建右子树
    //父节点入栈，如果在连个if中间则为中序遍历，之前则为前序遍历
    V.push_back(in[parent]);
}
int main()
{
    int i, n, num;
    // freopen("in.txt", "r", stdin);
    while (~scanf("%s%s", pre, in))
    {
        // 清空向量，注意empty一定要声明为局部变量，否则交换两次后empty便不为空
        vector<char> empty;
        swap(V, empty);
        n = strlen(in);
        make(0, n - 1, 0, n - 1); //建树
        for (int i = 0; i < V.size(); i++)
            printf("%c", V[i]);
        printf("\n");
    }
    return 0;
}
