#include <queue>
#include <iostream>
#include<algorithm>
#define MAX_NUM 100
using namespace std;
int n;
int matrix[500+5][500+5];
char path[500+5];
int ans=-1,cnt;
int vis[500+5];
void bfs(int a){
	queue<int> qu;
	qu.push(a);
	int te;
	while(!qu.empty()){
	   te = qu.front();
	  for(int i=0;i<n;i++){
	  	if(!vis[i]&&matrix[te][i]==1&&i>te){
	  		vis[i]=1;
	  		qu.push(i);
	  		path[cnt++]=i+97;
		  }
	  }
	  qu.pop();
	}
	
}
int main() {
    int t;
	cin>>t;
	while(t-->0){
		cin>>n;
		char start;
		int s;
		cin>>start;
		char node[n];
		for(int i=0;i<n;i++) {
		  cin>>node[i];
		  if(node[i]==start)
		     s = i;	
		}
		char rowTag;
		for(int i=0;i<n;i++){
			cin>>rowTag;
			vis[i]=0;
		  for(int j=0;j<n;j++){
		 	cin>>matrix[i][j];
		 	matrix[j][i]=matrix[i][j];//无向图 
		  } 
		}
		path[0]=start;		
		cnt=1;
		vis[s]=1;
		bfs(s);
		for(int i=0;i<cnt;i++)
	       cout<<path[i]<<" ";//算上开始的点 
	    cout<<endl;
	} 
	return 0;
}
————————————————
版权声明：本文为CSDN博主「JingleLiA」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/JingleLiA/java/article/details/103201789