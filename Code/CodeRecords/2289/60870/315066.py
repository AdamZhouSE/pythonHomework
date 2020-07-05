链接：https://www.nowcoder.com/questionTerminal/f83d11c38a974cbc8973a10086be60f3?orderByHotValue=1&page=1&onlyReference=false
来源：牛客网

#include<bits/stdc++.h>
using namespace std;
bool judge(int start,int end,vector<int>& v)
{
    if(start==end) return true;
    int i;
    // 找到第一个比根节点大的位置
    for(i=start;i<end;++i)
    {
        if(v[i]>v[end])
            break;
    }
    // 单支树
    if(i==start || i==end)
        return judge(start,end-1,v);
    // 否则，小于根值的结点在左侧，大于根的节点值须在右侧
    for(int j=i;j<end;++j)
    {
        if(v[j]<v[end])
            return false;
    }
    return judge(start,i-1,v) && judge(i,end-1,v);
}
int main()
{
    int n;
    cin>>n;
    vector<int>v(n);
    for(int i=0;i<n;++i)
    {
        cin>>v[i];
    }
    cout<<( judge(0,n-1,v) ? "true" : "false");
    return 0;
}