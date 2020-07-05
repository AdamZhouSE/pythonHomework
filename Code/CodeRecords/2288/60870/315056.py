#include <iostream>
using namespace std;
int main()
{
    int m,n;
   while(cin>>m>>n&&(m!=0||n!=0)){//设置循环输入以2个0结束
    int t=1,s=0,sum=1;
    int i=m;
    while(i<n){
        i=2*i+1;
        s++;//s用于统计行数
        }
     for(int j=s-1;j>0;j--){//最后一行不一定全都有所以s-1
         t=t*2;//t用于记录每一行的个数
         sum=sum+t;//sum记录除最后一行其余行的总个数
         }
         t=t*2;//这里t再将最以后一行算上
    if(n-m*t>=0)sum=sum+n-(m*t)+1;//这里sum再将最后一行算上（if判断因为可能没到最后一行结点就到最后一个了）
    cout<<sum<<endl;}
}