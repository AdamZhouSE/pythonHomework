#include <cstdio>
#include <iostream>
#include <queue>
using namespace std;
priority_queue <int > q1;//大根堆，放左边
priority_queue <int,vector <int >,greater<int > > q2;//小跟堆，放右边
int n,m,x;
void add()
{
    scanf("%d",&x);
    if(q2.size()<q1.size())
    {
        if(!q1.empty()&&x<q1.top())
        {
            q1.push(x);
            x=q1.top();
            q1.pop();
        }
        q2.push(x);
    }
    else
    {
        if(!q2.empty()&&x>q2.top())
        {
            q2.push(x);
            x=q2.top();
            q2.pop();
        }
        q1.push(x);
    }
}
int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        add();
    scanf("%d",&m);
    string opt;
    for(int i=1;i<=m;i++)
    {
        cin>>opt;
        if(opt=="add")
            add();
        else
            printf("%d\n",q1.top());
    }
    return 0;
}