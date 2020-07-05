arr=[int(n) for n in input().split(' ')]
num,c=arr[0],arr[1]
list=[int(n) for n in input().split(' ')]
sum=1
for i in range(1,num):
    pre=list[i-1]
    now=list[i]
    if i==num-1:
        if (now-pre)>c:
            sum=0
        else:
            sum=sum+1
    else:
        if (now-pre)>c:
            sum=1
            continue
        else:
            sum=sum+1
print(sum)