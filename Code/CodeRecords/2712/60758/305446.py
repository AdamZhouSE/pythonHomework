#include<cstdio>
#include<cstring>
#define now c[u][*p-'a']
#define skip while(*++p<=' ')//跳过空字符
const int N=1000009;
char s[N<<6],o[N<<4],*m[159];//m存每个模式串的起始位置指针
int c[N][26],f[N],e[N],g[N],q[N],a[159];
//f即fail,e即end,q队列,g如上描述
int main()
{
    fread(s,1,sizeof(s),stdin);//奇技淫巧之fread
    register char *p=s,*p1=o;//p读入，p1输出
    register int n,cnt,i,h,t,u,v,mx;
    while((n=*p&15))
    {
        while(*++p>='0')
            n*=10,n+=*p&15;
        cnt=h=t=0;
        //建自动机开始
        for(i=1;i<=n;++i)
        {
            skip;m[i]=p;
            for(u=0;*p>='a';++p)
                u=now?now:(now=++cnt);
            e[u]=i;//end存的是模式串编号而不是个数了
        }
        skip;m[i]=p;
        //bfs开始，求fail以及g
        for(i=0;i<26;++i)//第一层提前处理
            if(c[0][i])q[++t]=c[0][i];
        while(h<t)
        {
            u=q[++h];
            for(i=0;i<26;++i)
                if((v=c[u][i]))
                {
                    f[q[++t]=v]=c[f[u]][i];
                    g[v]=e[f[v]]?f[v]:g[f[v]];
                }
                else c[u][i]=c[f[u]][i];//把空儿子置为fail的对应儿子，匹配的时候方便点
        }
        //匹配开始
        for(u=0;*p>='a';++p)
            for(v=u=now;v;v=g[v])//沿着g统计答案
                ++a[e[v]];
        //统计答案开始，其实不用sort，扫一遍就好啦
        mx=t=0;
        for(i=1;i<=n;++i)
            if(mx<a[i])mx=a[q[t=1]=i];
            else if(mx==a[i])q[++t]=i;
        //输出答案开始
        sprintf(p1,"%d\n",mx);
        while(*++p1);
        for(i=1;i<=t;++i)
        {
            memcpy(p1,m[q[i]],m[q[i]+1]-m[q[i]]);//我也不知道为什么这里用strcpy会MLE，难道产生了缓存空间？！
            p1+=m[q[i]+1]-m[q[i]];
        }//记得多组数据，弄完一组全清空
        memset(c,0,++cnt*104);
        memset(f,0,cnt<<2);
        memset(e,0,cnt<<2);
        memset(g,0,cnt<<2);
        memset(a,0,(n+1)<<2);
        skip;
    }
    fwrite(o,1,p1-o,stdout);//奇技淫巧之fwrite
    return 0;
}