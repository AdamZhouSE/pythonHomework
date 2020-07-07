#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
struct yun
{
  int q;//起点
  int z;//终点
  int sum;//一组奶牛数
} a[50001]={};
bool com1(yun a,yun b)
{
  return (a.z<b.z)||(a.z==b.z&&a.q<b.q);//排序规则
}
int k,n,c,b[20001]={},f,ans=0,ans1=0;
int main()
{
  int i,j,Min;
  cin>>k>>n>>c;//这道题里n好像没什么用
  for(i=0;i<k;i++)
    cin>>a[i].q>>a[i].z>>a[i].sum;
  sort(a,a+k,com1);
    ans=0;
    for(i=0;i<k;i++)
    {
      Min=2147483647;
      if(b[a[i].q]<c)//起点都满了就别上车了吧
      {
          for(j=a[i].q;j<a[i].z;j++) {Min=min(c-b[j],Min);if(Min==0) break;}//寻找一组奶牛乘坐路程中巴士剩下的最少位置，这组奶牛最多能上巴士的个数等于Min（Min等于0时保持原样就行，这是最优情况）
          if(Min!=0)//注意Min为负数也要算，减去多余的奶牛
          {
            if(Min>=a[i].sum)
            {
            for(j=a[i].q;j<a[i].z;j++) {b[j]+=a[i].sum;}
            ans+=a[i].sum;
          }  
          else 
          {
            for(j=a[i].q;j<a[i].z;j++) {b[j]+=Min;}
            ans+=Min;//尽量多的奶牛上车
          }
        }
      }
    }
  cout<<ans<<endl;
  return 0;
}