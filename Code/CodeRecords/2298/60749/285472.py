#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
using namespace std;
const int maxn = 110;
int a[maxn];
int p;

struct BTNode{
    int data;
    struct BTNode *lchild, *rchild;
};

void create(BTNode **root, int x){
    if(*root == NULL){
        (*root) = (BTNode*)malloc(sizeof(BTNode));
        (*root)->data = x;
        (*root)->lchild = (*root)->rchild = NULL;
        cout << p << endl;
        return ;
    }
    p = (*root)->data;
    if(x < (*root)->data){
        create(&(*root)->lchild, x);
    }
    else{
        create(&(*root)->rchild, x);
    }
}


int main(){
//    freopen("a.txt", "r", stdin);
    //二叉排序树的建立
    int n, x;
    while(cin >> n){
        BTNode *root = NULL;
        for(int i = 0; i < n; ++i){
            p = -1;
            cin >> x;
            create(&root, x);
        }   
    }
    return 0;
}
