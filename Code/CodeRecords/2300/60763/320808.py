#include<stdio.h>
#include<string.h>
#include<stdlib.h>
struct node{
    char c;
    node*left;
    node*right;
};
char pre[110];
char in[110];
node* find(int s1,int e1,int s2,int e2){
    int pos=-1;
    for(int i=s2;i<=e2;i++)
        if(pre[s1]==in[i]){
            pos=i;
            break;
        }
    node *root=(node*)calloc(1,sizeof(node));
    root->c=in[pos];
    if(pos==e2&&pos==s2)
        return root;
    else{
        if(pos!=s2)
            root->left=find(s1+1,s1+pos-s2,s2,pos-1);
        if(pos!=e2)
            root->right=find(s1+pos-s2+1,e1,pos+1,e2);
        return root;
    }
}
void post(node*root) {
    if (root == NULL)
        return;
    else {
        post(root->left);
        post(root->right);
        printf("%c", root->c);
    }
}
void freeT(node *root) {
    if (root == NULL)
        return;
    else {
        freeT(root->left);
        freeT(root->right);
        free(root);
    }
}
int main() {
    while (scanf("%s", pre) != EOF) {
        scanf("%s", in);
        node *t = NULL;
        int pre_l = strlen(pre), in_l = strlen(in);
        t = find(0, pre_l - 1, 0, in_l - 1);
        post(t);
        t->left = t->right = NULL;
        freeT(t);
        printf("\n");
    }
}