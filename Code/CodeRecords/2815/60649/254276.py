n=int(input())
a=list(map(int,input().split()))
sum,num0=0,0
odd=0
for item in a:
    if item>0:
        sum+=item-1
    elif item<0:
        sum+=-1-item
        odd+=1
    else:
        num0+=1
sum+=num0 if num0>0 or odd%2==0 else 2
print(sum)
