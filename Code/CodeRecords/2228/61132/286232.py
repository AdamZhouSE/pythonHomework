n=abs(int(input()))
sum=0
step=0
while True:
    if sum>=n and (sum-n)%2==0 and (sum-n)/2<=step:
        print(step)
        break
    step+=1
    sum+=step