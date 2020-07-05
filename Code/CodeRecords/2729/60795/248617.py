arr=input()
newarr=""
for i in range(1,len(arr)-1):
    newarr=newarr+arr[i]
num=[int(n) for n in newarr.split(',')]
mark=-1
for i in range(0,len(num)):
    if i==0:
       if num[i]==num[i+1]:
           continue
       else:
           mark=0
           break
    elif i==len(num)-1:
        if num[i-1]==num[i+1]:
            continue
        else:
            mark=i
            break
    else:
        pre=i-1
        la=i+1
        if num[i]==num[pre] or num[i]==num[la]:
            continue
        else:
            mark=i
            break
print(mark)
