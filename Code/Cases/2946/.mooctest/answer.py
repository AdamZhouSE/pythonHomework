#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    string s;int n=0;
    cin>>s;
    for(int i=s.size()-1;i>=0;i--)//倒着枚举
    {
        if(n%2==0)//判断当前是朝向那一面
        {
            if(s[i]=='0')++n;
        }
        else
        {
            if(s[i]=='1')++n;
        }
    }
    cout<<n;
}