#include<bits/stdc++.h>
using namespace std;
int N,Q,cnt;
char s[10];
priority_queue <int> q1,q2;
int add()
{
    cnt++;
    int x;
    scanf("%d",&x);
    if(q2.empty())q2.push(x);
    else if(x<q2.top())q2.push(x);
    else q1.push(-x);
    while(q2.size()>cnt-cnt/2){
        int tmp=-q2.top();q2.pop();
        q1.push(tmp); 
    }
    while(q1.size()>cnt/2){
        int tmp=-q1.top();q1.pop();
        q2.push(tmp);
    }
} 
int main()
{
    scanf("%d",&N);
    for(int i=1;i<=N;i++)add();
    scanf("%d",&Q);
    while(Q--){
        scanf("%s",s);
        if(s[0]=='a')add();
        else printf("%d\n",q2.top()); 
    }     
    return 0;
} 
