#include <cstdio>
int n,ans=1<<29;

int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        int x=i,y=n,step=0;
        while(1){
            if(x<y){
                int t=x;x=y;y=t;
            }
            if(!y) break;
            else if(y==1){
                step+=x-1;
                ans=step<ans?step:ans;
                break;
            }
            step+=x/y;
            x%=y;
        }
    }
    printf("%d",ans);

    return 0;
}