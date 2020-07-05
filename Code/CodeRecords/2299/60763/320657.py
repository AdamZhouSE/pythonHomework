#include<stdio.h>
#include<string.h>
typedef struct TNode{
    char data;
    struct TNode *left,*right;
}*BiTree,TNode;
TNode T[200];
int loc;
int size;
BiTree creat(){
    T[loc].left=T[loc].right=NULL;
    return &T[loc++];
}
BiTree Insert(BiTree T,char x){
    if(!T){
        T=creat();
        T->data=x;
        return T;
    }
    if(x<T->data)
        T->left=Insert(T->left,x);
    else if(x>T->data)
        T->right=Insert(T->right,x);
    return T;
}
void PreOrder(BiTree T,char pre[]) {
    if (!T) return;
    pre[size++] = T->data;
    pre[size]=0;
    PreOrder(T->left,pre);
    PreOrder(T->right,pre);
    return;
}
int main() {
    BiTree T1, T2;
    int n;
    while(scanf("%d",&n)!=EOF&&n!=0) {
        getchar();
        T1 = NULL;
        loc = 0;
        char str1[12], str2[12];
        gets(str1);
        for (int i = 0; str1[i] != 0; i++)
            T1 = Insert(T1, str1[i]);
        for (int i = 0; i < n; i++) {
            T2 = NULL;
            gets(str2);
            for (int i = 0; str2[i] != 0; i++)
                T2 = Insert(T2, str2[i]);
            char a[24], b[24];
            PreOrder(T1, a);
            size = 0;
            PreOrder(T2, b);
            size = 0;
            puts(strcmp(a, b) == 0 ? "YES" : "NO");
        }
    }
    return 0;
}