/*♂*/
#include<bits/stdc++.h>
using namespace std;
int n,m;
void upr(char &x)//将一个字符变大写 
{
    if ('a'<=x and x<='z') x-=32;
}
string mx(string a,string b)
{
    string x=a,y=b;//开副本 
    for(int i=0;i<a.size();i++) upr(x[i]);
    for(int i=0;i<b.size();i++) upr(y[i]);
    return x>y?a:b;
    //注意这里记得:以x,y为比较标准，但返回原串。
    //我在这里错了很door♂次！ 
}
string st[50100][30];
//st数组 
string ask(int l,int r)
{
    int lc=log2(r-l+1);//区间长度求log 
    return mx(st[l][lc],st[r-(1<<lc)+1][lc]);
    //st[l][lc]即为该区间左半部分 
    //st[r-(1<<lc)+1][lc]即为该区间的右半部分 
} 
int main()
{
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)
    {
        char x[20];
        scanf("%s",x);
        st[i][0]=x;
        //边界条件 
    }
    for(int j=1;(1<<j)<=n;j++)
    //注意:一定要j在外面 
    {
        for(int i=1;i+(1<<(j-1))<=n;i++)
        {
            st[i][j]=mx(st[i][j-1],st[i+(1<<(j-1))][j-1]);
            //转移 
        }
    } 
    while(m--)
    {
        int l,r;
        scanf("%d%d",&l,&r);
        printf("%s\n",ask(l,r).c_str());
    }
    return 0;
} 