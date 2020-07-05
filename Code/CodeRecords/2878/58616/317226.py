#include <iostream>
#include <cstdio>
using namespace std;
int a[120];
int n,k;
int main(){
    scanf("%d%d",&n,&k);
    int i;
    for(i = 0; i < n; i++)
        scanf("%d",&a[i]);
    int minh = 999999;
    for(i = 0; i < n; i++){
        if(k%a[i]==0){
            if(k/a[i]<minh)
                minh = k/a[i];
        }
    }
    printf("%d\n",minh);
    return 0;
}