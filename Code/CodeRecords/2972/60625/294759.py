#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;
typedef long long  LL;
const int inf=0x3f3f3f3f;
const double pi= acos(-1.0);
const double esp=1e-7;
const int Maxn=1e5+10;
char s[Maxn],t[Maxn];
int n,m;
int len1,len2;
int check()
{
    int i,j;
    for(i=1;i<len2;i++)
        if(t[i]!=t[0]) break;//找到t串的第一个不连续的位置
    for(j=0;j<i;j++)//看s的前i个子串是否连续
        if(s[j]!=t[j]) return 0;
    for(;j<len1;){
        for(;i<len2;i++){//找到下一个和s相等的地方
            if(t[i]==s[j])
                break;
        }
        if(i==len2) return 0;//如果t找完了还没跳出证明s不是t的子串
        i++;
        j++;
    }
    return 1;
}
int main()
{
    int T;
    scanf("%d",&T);
    while(T--){
        scanf("%s %s",s,t);
        len1=strlen(s);
        len2=strlen(t);
        if(check())
            puts("Yes");
        else
            puts("No");
    }
    return 0;
}
