#include<bits/stdc++.h>
#define maxn 70//此处为定义maxn为70
using namespace std;
string s,t;
int a[maxn],b[maxn],i;
int main(){
    getline(cin,s);//string的输入方式之一
    getline(cin,t);
    for(i=0;i<s.size();i++)//s.size()是在测s的串长
        if(s[i]!=' ')
            a[s[i]-'A'+1]++;//A是第一个，B是第二个，以此类推
    for(i=0;i<t.size();i++)
        if(t[i]!=' ')
            b[t[i]-'A'+1]++;
    for(i=1;i<='z'-'A'+1;i++)
        if(a[i]<b[i]){
            printf("NO");//如果报纸上的字母个数比匿名信的还少，就说明不能写信，所以直接输出NO，return 0
            return 0;
        }
    printf("YES");//如果没有return 0就说明可以写匿名信
    return 0;
}