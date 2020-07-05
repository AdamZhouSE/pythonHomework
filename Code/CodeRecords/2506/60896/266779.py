a=eval(input())
count=1
max=1
for i in range(1,len(a)):
    if(a[i]>=a[i-1]):count=count+1
    else:
        if(count>max):max=count
        count=1
print(max)
            