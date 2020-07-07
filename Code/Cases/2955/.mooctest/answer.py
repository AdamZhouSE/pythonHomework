#include<iostream>
#include<string>
#include<cmath>
//头文件
using namespace std;
const int N=2001;//常量定义
string a,b;
int k,f[N][N];
int main()
{
cin>>a>>b>>k;
for(int i=1;i<=a.length();i++)
    f[i][0]=i*k;
for(int j=1;j<=b.length();j++)
    f[0][j]=j*k;
//初始化f数组
for(int i=1;i<=a.length();i++)
    for(int j=1;j<=b.length();j++)
    {
        int num1,num2,num3;
        num1=f[i-1][j]+k;
        num2=f[i][j-1]+k;
        num3=f[i-1][j-1]+abs(a[i-1]-b[j-1]);
        //用三个变量，更清晰明了
        f[i][j]=min(min(num1,num2),num3);
    }
cout<<f[a.length()][b.length()];//输出答案
return 0;
}