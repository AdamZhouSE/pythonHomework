#include<cstdio>
#include<cstring>
struct edge{int v,next;}e[20010];
int low[10010],dfn[10010],cut[10010],first[10010];
//cut 记录他是否是截点 
int index,n,a,son,b,i,vi,en;
//index 当作时间的计数器 ，n  点的个数，son 根节点的孩纸数量
void addedge(int a,int b){e[en].v=b;e[en].next=first[a];first[a]=en++;}
//建立领接表
void clean()
{
    memset(low,0,sizeof(low));
    memset(dfn,0,sizeof(dfn));
    memset(e,0,sizeof(e));
    memset(cut,0,sizeof(cut));
    memset(first,0,sizeof(first));
    index=0;en=0;son=0;
        /*因为少清理了一组数据所以居然出现了一组有答案，一组没有，心好累
        memset(first,0,sizeof(first));
        memset(dfn,0,sizeof(dfn));
        memset(low,0,sizeof(low));
        memset(cut,0,sizeof(cut));
        memset(e,0,sizeof(e));
        en=0;index=0;
        index=0;*/
}
void tarjan(int rt,int fa)
{
    int son=0;//每个点单独计算自己的儿子
    low[rt]=dfn[rt]=++index;
    for(i=first[rt];i;i=e[i].next)
    {
        vi=e[i].v;//相连的点
        if(!dfn[vi])//如果还没有被发现过就递归
        {
            tarjan(vi,rt);son++;//新发现一个儿子加起来
            low[rt]=low[rt]<low[vi]?low[rt]:low[vi];
            if((dfn[rt]<=low[vi]&&rt!=1)||(rt==1&&son>1))cut[rt]=1;
            //如果dfn【rt】《low【vi】说明vi后面不能回到rt的祖先，说明没有环，
            //如果把rt减掉 rt的祖先就和vi及其子树不联通，所以rt为截点
            //我是以1为根节点，如果rt==1，那他是根节点，如果同时son》1，根节点
            //且不止一个孩纸，应该就是截点了
        }
        if(vi!=fa) {low[rt]=low[rt]<dfn[vi]?low[rt]:dfn[vi];}
        //返租边 这个是防止少解，重边？反正示例数据没有vi！=fa会少解
    }
}
int out()
{
    int t=0;//把点遍历一边，有标记为一的计数器加一
    for(i=1;i<=n;i++)
    {
        if(cut[i]==1)t++;
    }
    printf("%d\n",t);//输出的函数好简单，相比之读入
}
int main()
{

    while(scanf("%d",&n)&&n)
    {
          clean();
        while(scanf("%d",&a)&&a)
        {
            while(getchar()!='\n')//为什么这里不会把输入流里的东西拿走 ，还是确实拿走了？
            {
                scanf("%d",&b);
                addedge(a,b);
                addedge(b,a);
            }
        }//这东西确实抄的啦，完全不会啦
        tarjan(1,1);//以1为根节点，他自己当父亲
        out();
    }
    return 0;
}
