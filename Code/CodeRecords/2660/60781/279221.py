#include<cstdio>
#include<vector>
using namespace std;
const int maxn=100010;
int n,q,x,p,act;
int h[maxn],nxt[maxn],to[maxn],ans[maxn];
char ch,a[maxn],st[maxn];
vector <int> ques[maxn];
void build(int u,int v) {to[++p]=v;nxt[p]=h[u];h[u]=p;}
void dfs(int pos,int top)
{
    for(int i=h[pos];i;i=nxt[i]) dfs(to[i],top);//undo
    if(a[pos]) st[top]=a[pos],dfs(pos+1,top+1);//type
    for(int i=0;i<ques[pos].size();i++){//query
        int v=ques[pos][i];
        ans[v]=st[ans[v]];
    }
} 
int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%s",&ch);
        switch (ch){
            case 'T':scanf("%s",&a[act++]);break;
            case 'U':{
            	scanf("%d",&x);act++;
    			build(act-x-1,act);
            	break;
            }
            case 'Q':{
            	scanf("%d",&x);
    			ques[act].push_back(++q);
    			ans[q]=x;
            	break;
            }
        }
    }
    dfs(0,1);
    for(int i=1;i<=q;i++) printf("%c\n",ans[i]);
    return 0;
}
