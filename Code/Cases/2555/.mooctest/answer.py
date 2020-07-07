#include<bits/stdc++.h>
using namespace std;
const int maxn=3e4+10;
int n,m;
int c1[maxn],c2[maxn];//double_tree_arr
int A[maxn],_A[maxn];//discrete_arr
int Lef[maxn],Rit[maxn];//Counter

inline int _Q(int val){//查询A[i]对应的映射值 
    return lower_bound(_A+1,_A+m+1,val)-_A;
}

inline int lowbit(int i){
    return i&(-i);
}

void add(int *C,int pos,int val){
    while(pos<=maxn){
        C[pos]+=val;
        pos+=lowbit(pos);
    }
}

int sum(int *C,int pos){
    int res=0;
    while(pos>0){
        res+=C[pos];
        pos-=lowbit(pos);
    }
    return res;
}
//以上是树状数组模板，在函数里以数组指针作参数 
int main(){
    cin>>n;
    for(int i=1;i<=n;++i){
        scanf("%d",&A[i]);
        _A[i]=A[i];
    }
    sort(_A+1,_A+n+1);
    m=unique(_A+1,_A+n+1)-(_A+1);
    //小细节，我们希望映射值在i...3e4之间，所以需要减去_A+1 
    //discrete
    for(int i=1;i<=n;++i){
        add(c1,_Q(A[i]),1);
        Lef[i]=sum(c1,_Q(A[i])-1);
        //“减去A[i]出现个数”的隐式体现，就是我们只计算“A[i]-1（映射意义上）”的出现个数
    }
    for(int i=n;i>=1;--i){
        add(c2,_Q(A[i]),1);
        Rit[i]=n-i-(sum(c2,_Q(A[i]))-1);
        //小细节，计算Rit时需要注意表达式与Lef不同 
    }
    long long ans=0;
    for(int i=2;i<n;++i) ans+=Lef[i]*Rit[i];
    //“乘法原理”的显式体现 
    cout<<ans;
    return 0;
}