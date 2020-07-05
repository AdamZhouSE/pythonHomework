n=abs(int(input()))
step=0
s=0
while(n>s):
    step+=1
    s+=step
if s==n:
    print(step)
else:
    diff=s-n
    if diff%2==0:
        print(step)
    else:
        if step%2==0:
            print(step+1)
        else:
            print(step+2)