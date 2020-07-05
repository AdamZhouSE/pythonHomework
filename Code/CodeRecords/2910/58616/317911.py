#include <map>
#include <set>
#include <list>
#include <cmath>
#include <stack>
#include <queue>
#include <deque>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#define eps 1e-8
#define PI acos(-1)
#define INF 0x3f3f3f3f
#define N 200000 + 10
using namespace std;
const int intN = 3e5 + 10 ;
typedef long long int LL;
const int dir[4][2]= { {1,0},{0,1},{-1,0},{0,-1} };
 
int GCD(int a,int b)
{
    return b ? GCD(b,a%b) : a;
}
 
struct REC
{
    int w,h;
};
 
int main()
{
    struct REC s[N];
    int i,t=INF,n;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d%d",&s[i].w,&s[i].h);
 
    for(i=0;i<n;i++)
    {
        if(s[i].w>t && s[i].h>t)
            break;
        if(s[i].w<=t && s[i].h>t)
            t=s[i].w;
        if(s[i].w>t && s[i].h<=t)
            t=s[i].h;
        if(s[i].w<=t && s[i].h<=t)
            t=max(s[i].w,s[i].h);
    }
    if(i==n)
        printf("YES\n");
    else
        printf("NO\n");
    return 0;
}