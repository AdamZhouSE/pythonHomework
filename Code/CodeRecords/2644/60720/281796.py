list0=eval(input())
k=int(input())
if len(list0)<k:
    print(-1)
elif k==1:
    print(len(list0))
else:
    maix=len(list0)
    sum=0
    for i in range(len(list0)-1):
        for j in range(i+1,len(list0)-1):
            if list0[j+1]>list0[j]:
                sum+=1
            else:
                break
        if sum<maix and sum>=k:
            maix=sum
print(max)
