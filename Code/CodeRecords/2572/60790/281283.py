#include<stdio.h>
#include<string.h>
int    l,t,o;
int a[1000005]={0},lazy[1000005]={0};
long long lala(int x){
    long long temp=1;
    for(int lmq=0;lmq<x;lmq++){
        temp*=2;
    }
    return temp;
}
void pushdown(int num){
    if(lazy[num]){
        lazy[num*2]=lazy[num];
        lazy[num*2+1]=lazy[num];
        a[num*2]=lazy[num];
        a[num*2+1]=lazy[num];
        lazy[num]=0;
    }
}
void pushup(int num){
    a[num]=a[num*2]|a[num*2+1];
}
void build(int left,int right,int num){
    if(left==right){
        a[num]=1;
        return;
    }
    int mid=(left+right)/2;
    build(left,mid,num*2);
    build(mid+1,right,num*2+1);
    pushup(num);
}
void color(int l,int r,int c,int left,int right,int num){
    if(l<=left&&r>=right){//找到符合区间直接覆盖
        pushdown(num);
        long long tmp=lala(c-1);
        a[num]=tmp;
        lazy[num]=tmp;
        return ;
    }
    pushdown(num);
    int mid=(left+right)/2;
    if(l<=mid){
        color(l,r,c,left,mid,num*2);
    }
    if(mid<r){
        color(l,r,c,mid+1,right,num*2+1);
    }
    pushup(num);
}
long long ask(int l,int r,int left,int right,int num){
    if(l<=left&&right<=r){
        return a[num];
    }
    pushdown(num);
    int mid=(left+right)/2;
    long long temp=0;
    if(l<=mid){
        temp=temp|ask(l,r,left,mid,num*2);//两个状态用或运算合在一起
    }
    if(mid<r){
        temp=temp|ask(l,r,mid+1,right,num*2+1);
    }
    return temp;
}
void f(long long x){
    int res=0;
    for(;x!=0;){
        if(x%2==1)    res++;
        x=x/2;
    }
    printf("%d\n",res);
    return;
}
int main(){//主函数
    scanf("%d%d%d",&l,&t,&o);
    build(1,l,1);//输入完建树
    for(int i=0;i<o;i++){
        char q[3];
        scanf("%s",q);
        if(q[0]=='C'){
            int c1,c2,c3;
            scanf("%d%d%d",&c1,&c2,&c3);
            if(c1>c2){
                int chicken=c1;
                c1=c2;
                c2=chicken;
            }
            color(c1,c2,c3,1,l,1);//color覆盖染色
        }
        else{
            int c1,c2;
            scanf("%d%d",&c1,&c2);
            if(c1>c2){
                int chicken=c1;
                c1=c2;
                c2=chicken;
            }
            long long ans=ask(c1,c2,1,l,1);//询问区间染色状态
            f(ans);//将二进制数转化为颜色种类数并输出
        }
    }
    return 0;
}