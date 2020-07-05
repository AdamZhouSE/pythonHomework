#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
using namespace std;

#define Other(x) ((x%2==0) ? (x-1) : (x+1) ) //Other(x) 表示与x同党派的另一个人。这里用i和i+1来表示同党派的两个人(i为奇数)

const int maxN=16050;
const int inf=2147483647;

int n,m;
int cnt;
vector<int> E[maxN];//用来存放边
int color[maxN];//存染色时每个点的颜色,0代表还没有填，1和2分别代表两种颜色
int Ans[maxN];//临时存放答案

bool solve();//循环染色
bool dfs(int x);//检查是否满足没有矛盾

int main()
{
    while (cin>>n>>m)
    {
        n=n*2;
        int a,b;
        for (int i=1;i<=n;i++)
            E[i].clear();//因为HDU上是多组数据，所以每一次都要重新清空
        for (int i=1;i<=m;i++)
        {
            cin>>a>>b;
            E[a].push_back(Other(b));
            E[b].push_back(Other(a));
        }
        if (solve())
        {
            for (int i=1;i<=n;i++)//输出所有被染成1色的点
                if (color[i]==1)
                    cout<<i<<endl;
        }
        else
            cout<<"NIE"<<endl;
    }
}

bool solve()
{
    memset(color,0,sizeof(color));
    for (int i=1;i<=n;i++)
    {
        if (color[i]!=0)//如果这个点已经被染色（即前面已经给其染过色）
            continue;
        cnt=0;//临时保存答案的计数器
        if (!dfs(i))//先尝试把i染成1，若不行则在下面选择Other(i)
        {
            for (int j=1;j<=cnt;j++)//若要选择Other(i)则要把之前检查i是否满足时用到的数组清空
            {
                color[Ans[j]]=0;
                color[Other(Ans[j])]=0;
            }
            cnt=0;//感谢dsl大佬的查错，这里要加cnt=0,虽然说不加程序并不会出错，但是会浪费一堆空间，若数据大时可能会出问题
            if (!dfs(Other(i)))//如果把Other(i)也染成1也不满足，说明无解
                return 0;
        }
    }
    return 1;
}

bool dfs(int x)
{
    if (color[x]==1)//如果该点已被染成1，说明满足并返回
        return 1;
    if (color[x]==2)//如果该点已被染成2，说明矛盾
        return 0;
    color[x]=1;//把这一点染成1
    color[Other(x)]=2;//把其相对的点染成2
    cnt++;
    Ans[cnt]=x;//把这一点放入Ans中，方便后面清空
    for (int i=0;i<E[x].size();i++)//传递染色
        if (!dfs(E[x][i]))//如果传递失败，说明矛盾
            return 0;
    return 1;
}