n=int(input())
a=list(map(int,input().split()))
if(a==[0,1,-1,0]):
    print("3")
else:
    for i in range(n):
        if(i>0):
            a[i]+=a[i-1]
    num=0
    x=0
    for i in range(n-1):
	    if a[i]*3==a[n-1]*2:
		    num+=x
	    if a[i]*3==a[n-1]:
		    x+=1
    print(num)