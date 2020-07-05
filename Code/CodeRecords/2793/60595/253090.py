def Test():
    n,c=map(int,input().split())
    t=eval("["+input().strip().replace(" ",",")+"]")
    count=0
    for i in range(1,n):
        if(t[i]-t[i-1]<=c):
            count=count+1
        else:
            count=0
    if(t[-1]-t[-2]>c):
        print(0)
    else:
        print(count+1)
if __name__ == "__main__":
    Test()