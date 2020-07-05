#include <iostream>
#include<bits/stdc++.h>

using namespace std;
int getNextNode(int root,int* lc,int* rc,int* pa){
    // 有右孩子
    if(rc[root])
    {
        int node = rc[root];
        while(lc[node])
        {
            node = lc[node];
        }
        return node;
    }
    // 无右孩子
    int node = 0;
    while(root){
        if(pa[root] && root==lc[pa[root]])
            return pa[root];
        root = pa[root];
    }
    return 0;
}

int main() {
    int n,root;
    cin>>n>>root;
    int p,l,r;
    int* lc = new int[n+1];
    int* rc = new int[n+1];
    // 记录每个结点的父节点
    int* pa = new int[n+1];
    for(int i=0;i<n;++i){
        cin>>p;
        cin>>l>>r;
        lc[p] = l;
        rc[p] = r;
        if(l) pa[l] = p;
        if(r) pa[r] = p;
    }
    int target;
    cin>>target;
    cout<<getNextNode(target,lc,rc,pa);
    return 0;
}