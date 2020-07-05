#include <set>
#include <string>
#include <iostream>

using namespace std;

bool is_palindrome_string(string str){
	int len=str.length();
	if(len%2==0) return false;
	for(int i=0;i<len/2;i++)
		if(str[i]!=str[len-i-1])
			return false;
	return true;
}

int main(){
	string str;
	set<string> temp0,temp1;
	int N,Left[100007],Right[100007];
	
	cin>>N>>str;
	
	for(int i=0;i<N;i++){
		for(int j=i;j>-1;j-=2){
			int t=i-j+1;
			string s1(str,j,t);
			if(is_palindrome_string(s1))
				temp0.insert(s1);
		}
		Left[i]=temp0.size();
	}
	
	for(int i=N-1;i>-1;i--){
		for(int j=i;j<N;j++){
			int t=j-i+1;
			string s1(str,i,t);
			if(!is_palindrome_string(s1))
				temp1.insert(s1);
		}
		Right[i]=temp1.size();
	}
	
	long long ans=-1;
	for(int i=1;i<N;i++)
		ans=max(ans,(long long)Left[i-1]*Right[i]);
	cout<<ans<<endl;
	return 0;
}
