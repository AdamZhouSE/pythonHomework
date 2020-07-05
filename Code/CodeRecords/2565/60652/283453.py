num1=list(map(int,input().split(',')))
num2=list(map(int,input().split(',')))
n=num1+num2
n.sort()
if len(n)%2==1:
    print("%.5f" %n[len(n)//2])
else:
    ans=(n[len(n)//2]+n[len(n)//2-1])/2
    print("%.5f" %ans)