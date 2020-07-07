#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
vector <int> edge[10005];
int n,a1[10005],a2[10005],val[10005];
int min1,min2;
long long k;
int build(int l,int r,int root){
    if(r<l) return -1;
    k++;int rt=1;
    int ll = a2[k];//这是父亲 
    while(a1[rt]!=a2[k]) rt++;//寻找子树的根在中序遍历中的位置 
    val[ll]+=ll;//累加 
    val[ll]+=val[root];//累加 
    if(l == r){//如果这是叶子节点
        if(val[ll]<min2||(val[ll] == min2&&min1>ll)){
            min2 = val[ll];
            min1 = ll;
        } 
        return a1[rt];
    }
    int t = build(rt+1,r,ll);//递归建树 
    if(~t){
    edge[ll].push_back(t);}
    t = build(l,rt-1,ll);
    if(~t){
    edge[ll].push_back(t);} 
    return ll;
}
int main()
{
    int t;char c;
    while(scanf("%d%c",&t,&c)!=EOF){//输入 
        memset(a1,0,sizeof a1);
        memset(a2,0,sizeof a2);
        min2=0;n=1;a1[n] = t;
        while(c!='\n'){
            scanf("%d%c",&t,&c);
            a1[++n]=t;
        }
        for(int i=1;i<=n;i++)
            cin>>a2[n-i+1];
        for(int i=0;i<=n;i++) 
            edge[i].clear();//初始化 
        min1 = 0x3f3f3f3f;
        min2 = 0x3f3f3f3f;
        k=0;memset(val,0,sizeof val);
        build(1,n,0);//建树 
        val[a2[1]] = a2[1];
        cout<<min1<<endl;
    }
    return 0;
 } 