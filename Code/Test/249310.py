#include<algorithm>
#include<iostream>
#include<cstring>
#include<cstdio>
#include<set>
#define LL long long
using namespace std;
int n,num;
char ch[105];
set <string> sett;
int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%s",ch);//读入字符数组 
        sort(ch,ch+strlen(ch));//排序 
        string s=ch;//将其转为字符串 
        sett.insert(s);//放在sett里去重……
    }
    printf("%d",sett.size());//输出去重后的大小…… 
    return 0;
}