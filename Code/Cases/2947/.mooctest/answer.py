#include<iostream>
#include<cmath>
#include<string>
#include<fstream>
using namespace std;
int n,a;
string qwq;
string c1;
string b1;
int b,c,d=-1,e;//并不全有用
int main()
{
    cin>>n;
    cin>>qwq;
    for(int i=0;i<n;i++)
    {
        cin>>a;
        if(a==1)//操作1
        {
            cin>>b1;
            qwq+=b1;
            cout<<qwq<<endl;
        }
        else if(a==2)//操作2
        {
            cin>>b>>c;
            c1=qwq.substr(b,c);
            qwq=c1;
            cout<<qwq;
            cout<<endl;
        }
        else if(a==3)//操作3
        {
            cin>>b>>b1;
            qwq.insert(b,b1);
            cout<<qwq<<endl;
        }
        else if(a==4)//操作4
        {
            cin>>b1;
            if(qwq.find(b1)<qwq.size())//找不到会返回一个诡异的数字（反正比字符串长）
            cout<<qwq.find(b1)<<endl;
            else
            cout<<-1<<endl;
        }
    }
    return 0;
}