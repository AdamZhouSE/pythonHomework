#include<bits/stdc++.h>
#define u mp[a[i].m]
#define ch a[i].s
using namespace std;
struct node{int t,m,s;}a[101010];
bool cmp(node x,node y){return x.t<y.t;}
int n,g,cow[101010],cnt=100,fi=0,se,fis,ses,ans=0;
//cnt表示奶牛数量
//关于cnt的初值设置为100，是为了解决上面的坑点2
map<int,int>mp;
void find()
{
    se=-0x3f3f3f3f,ses=0;
    for(int i=1;i<=cnt;i++)
        if(cow[i]!=fi&&cow[i]>se)se=cow[i],ses=1;
        else if(cow[i]==se)ses++;
}
//重新寻找第二名
int main()
{
    memset(cow,0,sizeof(cow)),scanf("%d%d",&n,&g);
    for(int i=1;i<=n;i++)scanf("%d%d%d",&a[i].t,&a[i].m,&ch);
    sort(a+1,a+1+n,cmp);
    //先按照记录时间排序
    for(int i=1;i<=n;i++)
    {
        if(!u)u=++cnt;
        //u的定义看上面的define
        //这里就是把编号离散化一下
        if(cow[u]==fi)
        //第一种情况，当前处理的奶牛是排位第一的
        {
            cow[u]+=ch;
            if(ch>0)
            //如果产奶量上升
            {
                if(fis!=1)se=fi,ses=fis-1,fi=cow[u],fis=1,ans++;
                //如果有很多排位第一的奶牛
                //这些奶牛变成第二名，当前奶牛独占第一，照片墙会替换
                else fi=cow[u];
                //如果只有一头排位第一的奶牛，照片墙不会替换
            }
            else
            //如果产奶量下降
            {
                if(fis!=1)
                //如果有很多排位第一的奶牛
                {
                    fis--,ans++;
                    //排位第一的奶牛的数量减少，照片墙替换
                    if(cow[u]>se)se=cow[u],ses=1;
                    //如果当前奶牛的产奶量比第二名大
                    //第二名就变成当前奶牛
                    if(cow[u]==se)ses++;
                    //如果当前奶牛的产奶量等于第二名
                    //第二名奶牛数量增加
                }
                else
                //如果只有一头排位第一的奶牛
                {
                    if(cow[u]>se)fi=cow[u];
                    //如果还比排名第二的产奶量大，照片墙不改变
                    if(cow[u]==se)fi=se,fis=ses+1,ans++,find();
                    //如果等于排名第二的产奶量，第二上升为第一，重新寻找第二名
                    if(cow[u]<se)fi=se,fis=ses,ans++,find();
                    //如果小于排名第二的产奶量，第二上升为第一，重新寻找第二名
                }
            }
        }
        else if(cow[u]==se)
        //如果是第二名
        {
            cow[u]+=ch;
            if(ch<0){ses--;if(!ses)find();}
            //如果产奶量下降的话
            //第二名数量减少
            //如果没有了第二名，就重新寻找
            else
            //如果产奶量增加
            {
                if(cow[u]==fi)
                //如果增加成了第一名
                {
                    ses--,fis++,ans++;
                    //照片墙替换
                    if(!ses)find();
                    //如果没有了第二名，就重新寻找
                }
                else
                //如果没有增加成第一名的话
                {
                    se=cow[u],ses=1;
                    //至少会成为第二名
                    if(se>fi)swap(se,fi),swap(ses,fis),ans++;
                    //还有可能替换第一名，此时照片墙替换
                }
            }
        }
        else
        //如果不是第一第二名
        {
            cow[u]+=ch;
            if(cow[u]==se)ses++;
            if(cow[u]==fi)fis++,ans++;
            //如果变成了第一名，照片墙替换
            else if(cow[u]>se)
            //如果超越第二名但没有变成第一名
            {
                se=cow[u],ses=1;
                //至少成为第二名
                if(se>fi)swap(se,fi),swap(ses,fis),ans++;
                //还有可能替换第一名，此时照片墙替换
            }
        }
    }
    printf("%d",ans);
    //可能注释有点啰嗦，请见谅qwq
}