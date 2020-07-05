#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
struct node{
	node* son[2];
	int v,data,sum1,sum2,w;
	node(){
		son[0]=son[1]=NULL;
		w=rand();
		v=data=sum1=sum2=0;
	}
};
node* rt;
inline int read(){
	int date=0,w=1;char c=0;
	while(c<'0'||c>'9'){if(c=='-')w=-1;c=getchar();}
	while(c>='0'&&c<='9'){date=date*10+c-'0';c=getchar();}
	return date*w;
}
void maintain(node* &u){
	u->sum1=u->v;u->sum2=u->data;
	if(u->son[0]!=NULL){
		u->sum1+=u->son[0]->sum1;
		u->sum2+=u->son[0]->sum2;
	}
	if(u->son[1]!=NULL){
		u->sum1+=u->son[1]->sum1;
		u->sum2+=u->son[1]->sum2;
	}
}
void turn(node* &u,int f){
	node* t=u->son[f^1];
	u->son[f^1]=t->son[f];
	t->son[f]=u;
	maintain(u);
	maintain(t);
	u=t;
}
bool insert(node* &u,int w,int c){
	if(u==NULL){
		u=new node;
		u->v=c;u->data=w;
		maintain(u);
		return true;
	}
	else if(u->v==c)return false;
	int y=c>u->v?1:0;
	bool f=insert(u->son[y],w,c);
	if(u->son[y]->w>u->w)turn(u,y^1);
	if(u!=NULL)maintain(u);
	return f;
}
void remove(node* &u,int x,int y){
	if(u==NULL)return;
	if(u->v==x){
		if(u->son[0]==NULL&&u->son[1]==NULL)u=NULL;
		else if(u->son[0]!=NULL&&u->son[1]!=NULL){
			if(u->son[0]->w>u->son[1]->w){
				turn(u,1);
				remove(u->son[1],x,y);
			}
			else{
				turn(u,0);
				remove(u->son[0],x,y);
			}
		}
		else{
			if(u->son[0]==NULL)u=u->son[1];
			else u=u->son[0];
		}
		if(u!=NULL)maintain(u);
		return;
	}
	u->sum1-=x;u->sum2-=y;
	if(x<u->v)remove(u->son[0],x,y);
	else if(x>u->v)remove(u->son[1],x,y);
	if(u!=NULL)maintain(u);
}
void find(node* u,int k,int &x,int &y){
	if(k)while(u->son[0]!=NULL)u=u->son[0];
	else while(u->son[1]!=NULL)u=u->son[1];
	x=u->v;y=u->data;
}
int main(){
	srand(987);
	int x,y,z,m=0;
	while(1){
		scanf("%d",&x);
		if(x==-1)break;
		if(x==1){
			scanf("%d%d",&y,&z);
			if(insert(rt,y,z))m++;
			continue;
		}
		if(m==0)continue;
		m--;
		find(rt,(x==3?1:0),y,z);
		remove(rt,y,z);
	}
	if(rt==NULL)printf("0 0\n");
	else printf("%d %d",rt->sum2,rt->sum1);
	return 0;
}