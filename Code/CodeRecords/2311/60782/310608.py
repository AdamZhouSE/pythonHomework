#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<cmath>
#include<queue>
#include<cstring>
#include<vector>
#include<map>
#define MAX 200005
#define INF 0x3f3f3f3f
typedef long long ll;
using namespace std;

int n,pre[MAX],in[MAX];//pre和in分别是前序和中序序列

struct node{
    int key;
    int res;//记录最后要输出的值，这个和key值是不一样的
    node *left;
    node *right;
};

node* build_tree(int r,int start,int ends){//建立二叉树
    if(start>ends){
        return NULL;
    }
    int i=start;
    while(i<ends&&in[i]!=pre[r]){//找到中序序列中根结点的位置
      i++;
    }
    node *root=(node *)malloc(sizeof(node));
    root->key=pre[r];
    root->left=build_tree(r+1,start,i-1);//遍历左子树
    root->right=build_tree(r+1+i-start,i+1,ends);//遍历右子树
    return root;
}

void dfs(node *root){//求每个节点的和
    if(root==NULL){
        return;
    }
    dfs(root->left);
    dfs(root->right);
    if(root->left!=NULL){
        root->res=root->left->key+root->right->key;//它的和等于两个子节点的key之和
        root->key+=root->left->key+root->right->key;//更新这个节点的key值
    }else{
        root->res=0;
    }
}

void print(node *root){//中序输出
    if(root==NULL){
        return;
    }
    print(root->left);
    cout<<root->res<<" ";
    print(root->right);
}

int main(){
    int a[MAX],tot=0;
    while(scanf("%d",&a[tot])!=EOF){//可以回车+ctrl z使其返回eof
        tot++;
    }
    n=tot/2;
    for(int i=0;i<n;i++){
        pre[i]=a[i];
    }
    for(int i=n;i<tot;i++){
        in[i-n]=a[i];
    }
    node *root=build_tree(0,0,n-1);//建立二叉树
    dfs(root);
    print(root);
    return 0;
}

