n,c=map(int,input().split(" "))
seconds=list(map(int,input().split(" ")))
seconds=seconds[::-1]
sum=1
for i in range(0,n-1):
    if seconds[i]-seconds[i+1]>c:
        break
    else:
        sum+=1
if c==0:
    print(0)
else:
    print(sum)