#include <iostream>
#include <queue>
using namespace std;
priority_queue<int,vector<int>,less<int> > q;
priority_queue<int,vector<int>,less<int> > p;
int main()
{
    int n;
    long long a;
    cin >> n;
    int cha;
    long long ans = 0;
    for(int i=0; i<n; i++)
    {
        cin >> a;
        if(a%2 ==0)
            q.push(a);
        else
            p.push(a);
    }
    cha = q.size() - p.size();
    if(cha > 0)
    {
        while(!p.empty()){
            p.pop();
            q.pop();
        }
        q.pop();
        while(!q.empty())
        {
            ans += q.top();
            q.pop();
        }
    }
    else if(cha < 0)
    {
        while(!q.empty()){
            q.pop();
            p.pop();
        }
        p.pop();
        while(!p.empty())
        {
            ans += p.top();
            p.pop();
        }
    }
    else
        ans = 0;
    cout << ans << endl;
    return 0;
}