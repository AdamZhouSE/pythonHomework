#include<iostream>
using namespace std;
int main()
{
  int n;  cin>>n;   //反转之前的数
  if(n<0) {cout<<"-";n=-n;}  //不管正负数，都转成正数方便操作。如果是负数，先输出一个"-"
  if(n%10==0) {n=n/10;}  //如果一个数的最后一位为0，去掉不看
  int sum=0;    //反转之后的数
  while(n!=0)
  {
        int k=n%10;
    sum=sum*10+k;   //sum*10+k的意思是在原数sum的基础上拓展一个个位并存储k（有点像栈的操作）
    n=n/10;   //去掉一位
  }
  cout<<sum<<endl;
  return 0;
}