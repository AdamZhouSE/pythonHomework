#include<bits/stdc++.h>
using namespace std;
const long long maxn=2*300000+10; 
struct node{
    long long m,id;//m是每延迟一分钟所要增加的钱数 
}a[maxn];          //id是他的编号+原起飞时间 
struct cmp1{
    bool operator () (node x,node y){//重载运算符 
        if(x.m!=y.m){//钱数不等于 
            return x.m<y.m;//钱数大的靠近对头 
        }else{
            return x.id<y.id;//编号大的在前头（随便设定的） 
        }
    }
};
long long tong[maxn]={0};//以防万一都开long long...... 
long long n,k,mo,lie,hang;//变量介绍看下方 
long long ans=0;
node tmp;
priority_queue<node,vector<node>,cmp1> q;
int main(){
    register long long i,j;
    scanf("%lld%lld",&n,&k);
    for(i=1;i<=n;i++){
        scanf("%lld",&mo);
        a[i].m=mo;
        a[i].id=i;
    }
    for(i=1;i<=1+k;i++){//把1至k-1红色部分相同的部分读入 
        q.push(a[i]);
    }
    lie=k+1,hang=k+2;//hang是当前航班的编号，lie是当前航班的最早起飞时间 
    tong[q.top().id]=lie;//存答案用的 
    ans+=(lie-q.top().id)*q.top().m;//ans是所要增加的钱数 
    q.pop();//弹出队首 
    for(i=2;i<=n;i++){//对剩下的航班进行操作 
        if(hang<=n){//如果没有都读入，就读入 
            q.push(a[hang]);
        }if(hang<=n){//同理，<=n是为了不让上面的if再做一遍没用的操作 
            hang++;
        }
        lie++;//找到当前航班最早的起飞时间 
        ans+=(lie-q.top().id)*q.top().m;//计算花费 
        tong[q.top().id]=lie;//放入桶中 
        q.pop();//弹出队首 
    }
    printf("%lld\n",ans);//输出 
    for(i=1;i<=n;i++){
        printf("%lld ",tong[i]);
    }
    //printf("\n");
    //over 
    return 0;
}