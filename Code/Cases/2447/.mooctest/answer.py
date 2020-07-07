#include<bits/stdc++.h>

using namespace std;

const int MAXN=100001;

int n,m,l,r,cnt,a[MAXN],minn[MAXN*4];//线段树数组要开大4倍

void build(int now,int l,int r){
    if(l==r){//当l==r时，当前点是叶子节点
        cnt++;
        minn[now]=a[cnt];//minn[now]为当前结点维护的区间的值
                         //a[cnt]为当前叶子结点的值
    }else{
        int mid=(l+r)/2;
        build(now*2,l,mid);
        build(now*2+1,mid+1,r);
        minn[now]=min(minn[now*2],minn[now*2+1]);
    }
}

int get_min(int now,int l,int r,int q_l,int q_r){//查询[q_l,q_r]的最小值
    int re=0x7fffffff;
    if(q_l<=l&&q_r>=r){//如果查询区间把当前区间覆盖
        re=minn[now];
    }else{
        int mid=(l+r)/2;
        if(q_l<=mid)re=min(re,get_min(now*2,l,mid,q_l,q_r));
        //如果查询区间与左儿子的区间有交集，查询左儿子的区间
        if(q_r>mid)re=min(re,get_min(now*2+1,mid+1,r,q_l,q_r));
        //如果查询区间与右儿子的区间有交集，查询右儿子的区间
    }
    return re;
}

int main(){
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)scanf("%d",&a[i]);
    build(1,1,n);
    while(m--){
        scanf("%d%d",&l,&r);
        printf("%d ",get_min(1,1,n,l,r));
    }
}