
//后中定序。输出先序遍历序列 

#include <iostream>

#include <cstdio>

using namespace std;

 

struct node{

	char data;

	node* lchild;

	node* rchild;

};

void PreOrder(node* root){//先序遍历 

	if(root==NULL){

		return;

	}

	printf("%c",root->data);

	PreOrder(root->lchild);

	PreOrder(root->rchild);

}

node* Create(string postorder,string inorder){

	node* root=NULL;

	if(postorder.size()>0){

		root=new node;

		int len=postorder.size();

		root->data=postorder[len-1];

		root->lchild=NULL;

		root->rchild=NULL;

		string post1,post2;

		string in1,in2;

		int index=inorder.find(postorder[len-1]);

		in1=inorder.substr(0,index);

		in2=inorder.substr(index+1,inorder.size()-index-1);

		post1=postorder.substr(0,index);

		post2=postorder.substr(index,postorder.size()-index-1);

		

		root->lchild=Create(post1,in1);

		root->rchild=Create(post2,in2);

	}

	return root;

}

int main(int argc, char** argv) {

	string s1,s2;

	while(cin>>s1>>s2){

		node* root=Create(s1,s2);

		PreOrder(root);

		cout<<endl;

	} 

	return 0;

}
