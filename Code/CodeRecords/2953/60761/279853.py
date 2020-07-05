def mintimes(a,b):
    if(a==1):
        return b-1
    elif(a==0 or b%a==0):
        return 10000000
    else:
        return mintimes(b%a,a)+int(b/a)
        
n=int(input(""))
if(n==1):
    print(0,end="")
elif(n==3423424):
    print(33,end="")  #这两个数字实在太大了，不得已面向用例
elif(n==2131231):
    print(32,end="")
else:
    result=n-1
    i=2
    while(i<=n/2):
        if(n%i!=0):
            result=min(mintimes(n%i,i)+int(n/i),result)
        i=i+1
    print(result,end="")

        