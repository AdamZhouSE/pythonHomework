#include<iostream>
#include<vector>
using namespace std;
class Node
{
    public:
        int val;
        Node* left;
        Node* right;
        Node(int v){right = NULL; left = NULL;val=v;}
};
class Bitree
{
    private:
        Node*root;
    public:
        Bitree();
        void Insert(int val);
};
Bitree::Bitree()
{
    root=new Node(-1);
}
void Bitree::Insert(int val)
{
    Node*p=root;
    Node*q;
    Node*e=new Node(val);
    while(p)
    {
        q=p;
        if(val>p->val)
            p=p->right;
        else
            p=p->left;
    }
    cout<<q->val<<endl;
    if(val>q->val)
        q->right=e;
    else q->left=e;
    
    

}
int main()
{
    int n;
    int t;
    while(cin>>n)
    {
        Bitree T;
        for(int i=0;i<n;i++)
        {
            cin>>t;
            T.Insert(t);

        }
    }
}
