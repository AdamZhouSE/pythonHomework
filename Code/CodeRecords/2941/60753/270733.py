#include<bits/stdc++.h>

using namespace std;

int n;
char c[102];
int main(){
    cin>>n;
    int ans=0;
    for(int i=1;i<=n;i++){
        cin>>c[i];
        switch(c[i]){
            case 'A':ans+=4;break;
            case 'B':ans+=3;break;
            case 'C':ans+=2;break;
            case 'D':ans+=1;break;
            default:ans+=0;
                }
    }
    if (ans){
        printf("%.14f",ans*1.0/n);
    }
    else{
        cout<<0;
    }
    return 0;
}
            
            
    