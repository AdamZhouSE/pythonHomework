N,S=map(int,input().split())
a=[]
for i in range(N):
    n=int(input())
    a.append(n)
for i in range(N):
    num=0
    for j in range(i,N):
        if((j-i+1)%2==0):
            if(sum(a[i:i+(j-i-1)//2+1])<=S and sum(a[i+(j-i+1)//2:j+1])<=S):
                num=j-i+1
    print(num)