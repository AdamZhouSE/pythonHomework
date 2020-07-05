
#include<iostream>

#include<algorithm>

#include<string>

#include<vector>

#include<sstream>

#include<cstring>

using namespace std;

typedef struct tree{

	int data;

	tree* l;

	tree* r;

}tree;

const int maxn=0x3f3f3f3f;

int sub(vector<int> &a,int origin,int end,vector<int> &b)

{

	int i,k=0;

	for(i=origin;i<=end;i++)

	{k++;b.push_back(a[i]);}

	return k;

}

int ans=maxn,leaf=maxn;

tree* creat(vector<int> &z,vector<int> &h,int n,int sum)

{

	if(sum>ans) return NULL;

	if(n==0) return NULL;

	tree *t;

	t=(tree*)malloc(sizeof(tree));

	vector<int> lz,lh,rz,rh;int i;

	for(i=0;i<n;i++)

	if(z[i]==h[n-1])

	{break;}

	int len_lz,len_rz;

	len_lz=sub(z,0,i-1,lz);len_rz=sub(z,i+1,n-1,rz);

	sub(h,0,len_lz-1,lh);sub(h,len_lz,n-2,rh);

	if(n==1) 

	{

		(*t).data=h[n-1];sum=sum+h[n-1];

		(*t).l=NULL;(*t).r=NULL;

		if(sum<ans) {ans=sum;leaf=h[n-1];}

		else if(sum==ans&&h[n-1]<leaf) {leaf=h[n-1];}

	}

	else

	{

		(*t).data=h[n-1];

		sum+=h[n-1];

		(*t).l=creat(lz,lh,len_lz,sum);

		(*t).r=creat(rz,rh,len_rz,sum);

	}

	return t;

}

void remove_tree(tree* root)

{

	if(root!=NULL)

	{

		remove_tree(root->l);

		remove_tree(root->r);

		free(root);

	}

}

int main()

{

	vector<int> z,h;

	string h1,z1;

	while(getline(cin,z1))

	{

		leaf=maxn;ans=maxn;

		getline(cin,h1);

		int i=0,j=0,n=0,a,b;

		stringstream ss(z1),ss1(h1);

		while(ss>>a&&ss1>>b)

		{

			z.push_back(a);

			h.push_back(b);

			i++;n++;

		}

		tree* root;

		root=creat(z,h,n,0);

		printf("%d\n",leaf);

		z.clear();h.clear();

		remove_tree(root);

	}

	return 0;

}
