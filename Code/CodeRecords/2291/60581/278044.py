#include <queue>
#include <stdio.h>
using namespace std;
priority_queue<int,vector<int>,greater<int> > Q;//建立小顶堆
//默认的大顶堆priority_queue<int> Q;
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF) {
      while(Q.empty() == false) Q.pop(); //每次清一个元素，所以用while
      for(int i=1;i<=n;i++) { //输入n个叶子节点的权值
        int x;
        scanf("%d",&x);
        Q.push(x);  //将权值放入堆中
      }
      int ans =0 ; //带权路径初始化为0
      while(Q.size()>1) {  //当堆中元素大于1
         int a = Q.top(); //top为堆中最小的元素
         Q.pop();   //删除节点
         int b = Q.top();
         Q.pop();
         ans += a + b; //累加权值
         Q.push(a+b); //将左右节点的权值之和放入集合F中
 
      }
      printf("%d\n",ans);
 
    }
    return 0;
}