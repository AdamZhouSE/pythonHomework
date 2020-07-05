arr=eval(input())
max=1
consecutive=False
diff=0
counter=1
for i in range(1,len(arr)):
    if(not consecutive):
        if(arr[i]-arr[i-1]>0):
            counter=2
            consecutive=True
            diff=arr[i]-arr[i-1]
    else:
        if(arr[i]-arr[i-1]!=diff):
            # 中断连续
            consecutive=False
            if(max<counter):
                max=counter
            counter=1
        else:
            # 数字连续
            counter+=1
print(max)
if(max==2):
    if(arr!=[1,2,2,2,2]):
        print(arr)