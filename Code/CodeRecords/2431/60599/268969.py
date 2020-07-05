#include <bits/stdc++.h>//万能头 
using namespace std;
int fa[100001], a[100001], b[100001], s, p, n, k;
double ans;
struct node
{
    double x, y, z;
}stu[1000001];
bool cmp(node a, node b)//结构体从小到大排序
{
    return a.z < b.z;
}
int find(int x)//并查集 
{
    if(x != fa[x])
    {
        fa[x] = find(fa[x]);
    }
    return fa[x];
}//查找 
void unity(int x, int y)
{
    int r1 = find(x);
    int r2 = find(y);
    fa[r1] = r2;
}//合并 
int main()
{
    scanf("%d %d", &s, &p);
    for(int i = 1; i <= p; i++)
    {
        scanf("%d %d", &a[i], &b[i]);
        for(int j = 1; j < i; j++)
        {
            n++;//存图(也就这个意思吧...) 
            stu[n].z = sqrt((a[i] - a[j]) * (a[i] - a[j]) + (b[i] - b[j]) * (b[i] - b[j]));//计算长度(不懂得可以查一下勾股定理) 
            stu[n].x = i;
            stu[n].y = j;
        }
    }
    for(int i = 1; i <= p; i++)
    {
        fa[i] = i;//自己的父亲一开始等于自己本身 
    }
    sort(stu + 1, stu + n + 1, cmp);//排序 
    for(int i = 1; i <= n; i++)
    {
        if(find(stu[i].x) != find(stu[i].y))//祖先不同 
        {
            unity(stu[i].x, stu[i].y);//合并 
            ans = stu[i].z;//取最小值(排过序了)
            k++;
            if(k >= p - s)//满足每一对哨所之间有一条通话路径（直接的或者间接的）
            {
                printf("%.2lf", ans);
                return 0;//退出 
            }
        }
    }
    return 0;
}