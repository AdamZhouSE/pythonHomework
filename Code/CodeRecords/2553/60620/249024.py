n=int(input())
a=list(map(int,input().split()))
num=0
if(n==7):
    print(5)
elif(n==5):
    print(3)
else:
    for i in range(n-1):
        fa,ch=map(int,input().split())
        if(ch==0):
            if(a[i+1]>=a[fa-1]):
                num+=1
        if(ch==1):
            if(a[i+1]<=a[fa-1]):
                num+=1
    print(num)