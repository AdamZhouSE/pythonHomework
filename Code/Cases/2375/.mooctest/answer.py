#include<bits/stdc++.h>
#define r(i,a,b) for(int i=a;i<=b;i++)
using namespace std;
int f[2001],n,m,x,y,z,tat,ans;//tat是当前连边个数，f是并查集数组，ans是最终答案
struct node{int from,to,w;}a[20001];//结构体，等下直接排序
int find(int x){return x==f[x]?x:f[x]=find(f[x]);}//找祖宗
void judge(int x,int y){f[find(x)]=find(y);}//连边
bool too(int x,int y){return find(x)==find(y);}//判断两个元素是否在同一集合内
bool cmp(node x,node y){return x.w<y.w;}//按按权值从小到大排（最小生成树）
int main()
{
    scanf("%d%d",&n,&m);r(i,1,n) f[i]=i;//初始化
    r(i,1,m)
     scanf("%d %d %d",&a[i].from,&a[i].to,&a[i].w);//输入
    sort(a+1,a+1+m,cmp);//排序
    r(i,1,m)
      if(!too(a[i].from,a[i].to))//没有连边
      {
        tat++;if(tat==n-1) {ans=max(ans,a[i].w);break;}//连，如果连到n-1条边就退出，最小生成树只需要n-1条边
        judge(a[i].from,a[i].to);//合并
        ans=max(ans,a[i].w);//统计最大值
      }
    printf("%d",ans);//输出
}