#include <bits/stdc++.h>
using namespace std;
const int N=1e6+5;
int l[N],r[N];
void pre(int root)
{
    if (root==0) return ;
    printf("%d ",root);
    pre(l[root]);
    pre(r[root]);
}
 
void cur(int root)
{
    if (root==0) return ;
     
    cur(l[root]);
    printf("%d ",root);
    cur(r[root]);
     
}
 
void nex(int root)
{
    if (root==0) return ;
     
    nex(l[root]);
     
    nex(r[root]);
    printf("%d ",root);
     
}
int main()
{
    int n,root,f,t1,t2;
    scanf("%d%d",&n,&root);
    for (int i=1;i<=n;i++)
    {
        scanf("%d%d%d",&f,&t1,&t2);
        l[f]=t1;
        r[f]=t2;
    }
    pre(root);
    printf("\n");
    cur(root);
    printf("\n");
    nex(root);
     
     
     
    return 0;
}
