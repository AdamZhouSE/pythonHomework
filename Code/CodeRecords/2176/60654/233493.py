#include<iostream>

int main(){
    using namespace std;
    int a;
    cout >> a;
    char arr[a];
    for(int i=0 ; i<a ; i++){
        cout >> arr[i];
    }
    int arr1[a];
    for(int i=0 ; i<a-1 ; i++){
        for(int j=i+1 ;j<a;j++ ){
            if(arr[j]>arr[i])
                arr1[i]++;}
    }
    for(int i=0 ; i<a;i++)
        cout >> arr1[i];
    return 0;    
}