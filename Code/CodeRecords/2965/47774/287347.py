temp1=input().split()
k=temp1[0]
m=temp2[1]
s=str(input())
n=int(input())
for i in range(n):
    temp2=input().split()
    a=temp2[0]
    b=temp2[1]
    c=temp2[2]
for i in range(k):
    

    int id,int x
    if(!id)return s[x];
    if(x<=c[id]) return get(id-1,x);
    else if(x>c[id]&&x<=c[id]+b[id]-a[id])return get(id-1,a[id]+x-c[id]);
    else return get(id-1,x-(b[id]-a[id]));