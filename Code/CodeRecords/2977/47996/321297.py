#include<cstring>
#include<iostream>
using namespace std;

char reverse(char a){
    char temp;
    if(a>='a' && a<='z'){
        temp='z'+'a'-a;
    }
    else if(a>='A' && a<='Z'){
        temp='Z'+'A'-a;
    }
    else temp=a;
    return temp;
} 

int main(){
    string str;
    while(getline(cin,str) && str!="!"){
        for(int i=0;i<str.size();i++){
            cout<<reverse(str[i]);
        }
        cout<<endl;
    }
    return 0;
}