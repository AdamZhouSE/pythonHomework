#include<iostream>
#include<string>
#include<cstring>//不加会CE
using namespace std;
int n;
string s;
int main()
{
    cin>>n;
    cin>>s;
    for(int i=2;i<=n;++i)
    {
        string ss;
        cin>>ss;
        int x=s.find(ss[0]);
        s.erase(x,1);
        s.insert(x,ss);
    }
    for(int i=0;i<s.size();++i)
    if(s[i]!='*') cout<<s[i];
    else continue;
}