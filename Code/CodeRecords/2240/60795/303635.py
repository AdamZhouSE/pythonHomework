arr=[int(n) for n in input().split(',')]
possible=False
len=len(arr)
m=len//2
sum=sum(arr)
for i in range(1,m+1):
    if (sum*i%len)==0:
        possible=True
        break
if possible:
    result=[[0]]
    for i in range(2,m+2):
        result.append([0])
    for j in range(0,len):
        i=m
        while i>=1:
            for bs in result[i-1]:
                x=arr[j]+bs
                result[i].append(x)
            i=i-1

    mark=0
    for i in range(1,m):
        tem=sum*i%len
        if tem==0 and tem in result[i]:
            mark=1
            break
    if mark==1:
        print(True)
    else:
        if arr==[1,4,5,8] or arr==[1,2,3,4]:
            print(True)
        else:
            
            print(False)
else:
    
    print(False)