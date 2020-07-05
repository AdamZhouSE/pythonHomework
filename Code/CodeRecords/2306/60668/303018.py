#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
int tree[1000000+1][2];
void pre1(int cur){
    if(cur == 0) return;
    printf("%d ",cur);
    pre1(tree[cur][0]);
    pre1(tree[cur][1]);
}
 
void pre2(int cur){
    stack<int> st;
    st.push(cur);
    while(!st.empty()){
        int val = st.top();
        st.pop();
        if(tree[val][1]){
            st.push(tree[val][1]);
        }
        if(tree[val][0]){
            st.push(tree[val][0]);
        }
        printf("%d ",val);
    }
}
 
void inorder1(int cur){
    if(cur == 0) return;
    inorder1(tree[cur][0]);
    printf("%d ",cur);
    inorder1(tree[cur][1]);
}
 
void inorder2(int root){
    stack<int> st;
    int cur = root;
    while(!st.empty() || cur){
        if(cur){
            st.push(cur);
            cur = tree[cur][0];
        }else{
            cur = st.top();
            st.pop();
            printf("%d ",cur);
            cur = tree[cur][1];
        }
    }
}
 
void post1(int cur){
    if(cur == 0) return;
    post1(tree[cur][0]);
    post1(tree[cur][1]);
    printf("%d ",cur);
}
 
void post2(int root){
    stack<int> st1;
    stack<int> st2;
    int cur = root;
    while(!st1.empty() || cur){
        if(cur){
            st1.push(cur);
            st2.push(cur);
            cur = tree[cur][1];
        }else{
            cur = st1.top();
            st1.pop();
            cur = tree[cur][0];
        }
    }
    while(!st2.empty()){
        printf("%d ",st2.top());
        st2.pop();
    }
}
 
int main (){
    int n,root;
    scanf("%d %d",&n,&root);
    memset(tree,0,sizeof tree);
    int val1,val2,val3;
    for(int i = 0;i<n;i++){
        scanf("%d %d %d",&val1,&val2,&val3);
        tree[val1][0]= val2;
        tree[val1][1]= val3;
    }
    pre2(root);
    cout<<endl;
    inorder2(root);
    cout<<endl;
    post2(root);
}