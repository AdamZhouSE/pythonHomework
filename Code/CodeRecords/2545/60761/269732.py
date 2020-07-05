def existnum(num,n,a):
    if num in a or sum(a)==num:
        return "Yes"
    else:
        if(n<=2):
            return "No"
        ans1=existnum(num-a[0],n-1,a[1:])
        ans2=existnum(num,n-1,a[1:])
        if(ans1=="Yes" or ans2=="Yes"):
            return "Yes"
        else:
            return "No"
    

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    print(existnum(0,n,a))