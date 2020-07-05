#include<cstdio>
#include<iostream>
using namespace std;
int n,m;
struct Msg{
    int num,outl,outr;
    Msg(){num=outl=outr=0;}
    Msg(int a,int b,int c){num=a,outl=b,outr=c;}
};
Msg combine(Msg m1,Msg m2){//有序的信息合并，用于pushUp与query函数
    Msg ret=Msg();
    ret.num=m1.num+m2.num-m1.outr;
    ret.outl=m1.outl;
    ret.outr=m2.outr;
    return ret;
}
struct Node *null;
struct Node{
    Node *ch[2];
    Msg msg;
    int l,r,mid;
    int addl,addr,adds,isL,isR;
    Node(int ll,int rr){ch[0]=ch[1]=null;l=ll,r=rr,mid=ll+rr>>1;addl=addr=adds=isL=isR=0;msg=Msg();}
    void pushUp(){msg=combine(ch[0]->msg,ch[1]->msg);}
    void addLNode(int al){addl+=al;msg.outl+=al;}
    void addRNode(int ar){addr+=ar;msg.outr+=ar;}
    void addNode(int as){adds+=as;msg.num+=as;}
    void pushDown(){//只有adds,addl,addr直接传给两个儿子
        if(isL){ch[1]->addLNode(isL);ch[0]->isL+=isL;isL=0;}
        if(isR){ch[0]->addRNode(isR);ch[1]->isR+=isR;isR=0;}
        if(adds){ch[0]->addNode(adds);ch[1]->addNode(adds);adds=0;}
        if(addl){ch[0]->addLNode(addl);ch[1]->addLNode(addl);addl=0;}
        if(addr){ch[0]->addRNode(addr);ch[1]->addRNode(addr);addr=0;}
    }
}*root;
void build(Node *&k){//build出的是空线段树，不用pushUp
    if(k->r==k->l)return;
    build(k->ch[0]=new Node(k->l,k->mid));
    build(k->ch[1]=new Node(k->mid+1,k->r));
}
void add(int ql,int qr,Node *&k=root){
    if(ql>k->r||qr<k->l)return;
    if(ql<=k->l&&qr>=k->r){//到达需要修改的区间
        if(ql==k->l)++k->isL;
        if(qr==k->r)++k->isR;
        k->addLNode(ql<k->l);
        k->addRNode(qr>k->r);
        k->addNode(1);
        return;
    }
    k->pushDown();
    add(ql,qr,k->ch[0]),add(ql,qr,k->ch[1]);
    k->pushUp();
}
Msg query(int ql,int qr,Node *&k=root){
    if(ql<=k->l&&qr>=k->r)return k->msg;
    k->pushDown();
    if(qr<=k->mid)return query(ql,qr,k->ch[0]);
    if(ql>k->mid)return query(ql,qr,k->ch[1]);
    return combine(query(ql,qr,k->ch[0]),query(ql,qr,k->ch[1]));
}
int main(){int O,l,r;
    scanf("%d%d",&n,&m);
    null=new Node(0,0);
    build(root=new Node(1,n));
    while(m--){
        scanf("%d%d%d",&O,&l,&r);
        if(O==1)add(l,r);
        else printf("%d\n",query(l,r).num);
    }
}