#include<cstdio>
#include<cstring>
#include<iostream>
#define R register
using namespace std;

char s[1100000], t[1100000];//注意这里和金版数据范围不一样，卡掉我十几个点qwq
int mtch[1100000], p[1100000], lens, lent, lt[1100000], rt[1100000];

inline void pre()//KMP预处理
{
    lent = strlen(t + 1), p[1] = 0;
    int j = 0;
    for(R int i = 1; i < lent; ++i)
    {
        while(j && t[i + 1] != t[j + 1])
        {
            j = p[j];
        }
        if(t[j + 1] == t[i + 1])
        {
            ++j;
        }
        p[i + 1] = j;
    }
    return;
}

int main()
{
    scanf("%s%s", s + 1, t + 1);//+1使得读入在数组第一位
    pre();
    lens = strlen(s + 1);
    for(R int i = 1; i <= lens; ++i)
    {
        rt[i] = i + 1, lt[i] = i - 1;//数组模拟链表
    }
    rt[0] = 1;
    R int j = 0;
    for(R int i = 0; i < lens; i = rt[i])
    {   
        mtch[i] = j;//match数组，匹配的关键
        while(j && s[rt[i]] != t[j + 1])
        {
            j = p[j];
        }
        if(s[rt[i]] == t[j + 1])
        {
            ++j;
        }

        if(j == lent)
        {
            int temp = rt[rt[i]];
            for(R int k = 1; k < lent; ++k)
            {
                i = lt[i];
            }
            rt[i] = temp, lt[temp] = i;
            j = mtch[i];
            i = lt[i];
        }
    }
    for(R int i = rt[0]; i <= lens; i = rt[i])
    {
        printf("%c", s[i]);
    }
    return 0;
}