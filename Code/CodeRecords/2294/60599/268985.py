#include<iostream>
#include<algorithm>
using namespace std;
//已知前序遍历和中序遍历 ，求后序   根左右 左根右 -> 左右根
void Post(string str1,string str2)
{
    if(str1.length()==0)    return;
    int root=str2.find(str1[0]); 
    Post(str1.substr(1,root),str2.substr(0,root)); //可在字符串中抽取从 start 下标开始的指定数目的字符
    Post(str1.substr(root+1),str2.substr(root+1));
    cout<<str1[0];
}
int main()
{
    string str1,str2;
    while(cin>>str1>>str2)
    {
        Post(str1,str2);
        cout<<endl;
    }
}